# load libraries
library(tidyverse)    # CRAN v2.0.0
library(janitor)      # CRAN v2.2.0
library(estimatr)     # CRAN v1.0.0
library(binom)        # CRAN v1.1-1.1
library(readxl)       # CRAN v1.4.3
library(modelsummary) # CRAN v1.4.2
library(kableExtra)   # CRAN v1.3.4
library(ggsankey)     # [github::davidsjoberg/ggsankey] v0.0.99999
library(patchwork)    # CRAN v1.1.3
library(ggtext)       # CRAN v0.1.2
library(mice)         # CRAN v3.16.0
library(extrafont)    # CRAN v0.19
loadfonts()

# display options
options(pillar.sigfig = 5)

# source functions
source("R/functions.R")

# read data tables
df <- read_xlsx("data/hiring.xlsx")
df_candidates <- read_xlsx("data/candidates.xlsx")

#########################
#### data processing ####
#########################
# recode/rename gender and treatment variable
df_candidates$gender <- ifelse(df_candidates$gen == 1, "Female", "Male")
df$gender <- ifelse(df$gender == 1, "Female", "Male")
df <- df %>% mutate(treatment = as.character(treatapp1_choice)) %>% select(-treatapp1_choice)
df <- df %>% mutate(treatmentlabel = fct_reorder(
  factor(ifelse(treatment=="1", "italic('T'[fW])", "italic('T'[fK])")),
  treatment, ~mean(as.numeric(.x)))
)

# compute willingness to pay from single price list choices
df <- df %>%
  select(participant, contains("offer")) %>% 
  pivot_longer(cols = contains("offer"), names_to = "offer", values_to = "response") %>%
  mutate(offer = paste0(str_sub(offer, 1,4), "_", str_sub(offer, 10,11))) %>% 
  separate(offer, into = c("cert", "offer"), sep = "_") %>% 
  mutate(offer = as.numeric(offer)) %>% 
  group_by(participant, cert) %>% 
  summarise(price = ifelse(max(response)==0, 0, max(offer[response==1])*10),
            switching = ifelse(max(response)==0, FALSE, 
                               sum(offer[response==max(response)]) != sum(seq(1,max(offer[response==max(response)]),1))),
            .groups = "drop") %>% 
  pivot_wider(names_from = cert, values_from = c(price, switching)) %>% 
  mutate(price_know = ifelse(switching_know == TRUE, NA, price_know),
         price_word = ifelse(switching_word == TRUE, NA, price_word)) %>% 
  select(participant, contains("price")) %>% 
  left_join(df, ., by = "participant")

# create column that classifies explicit discrimination type
df <- df %>% 
  mutate(type = case_when(
    indif2 & indif3 ~ "non",
    dec2 & dec3     ~ "against_women",
    !dec2 & !dec3   ~ "against_men",
    TRUE            ~ "mixed"
  ))

# create column that classifies explicit discrimination type also for certificates
df <- df %>% 
  mutate(
    type_cert = case_when(
      indif4 & indif5 ~ "non",
      dec4 & dec5  ~ "against_word",
      !dec4 & !dec5 ~ "against_know",
      TRUE ~ "mixed")
  )

# create columns that classify explicit discrimination type alternatively
df <- df %>% 
  rowwise %>% 
  mutate(dec23_1st   = c(dec2, dec3)    [which.min(c(position2, position3))],
         dec23_2nd   = c(dec2, dec3)    [which.max(c(position2, position3))],
         indif23_1st = c(indif2, indif3)[which.min(c(position2, position3))],
         indif23_2nd = c(indif2, indif3)[which.max(c(position2, position3))]) %>% 
  ungroup %>% 
  mutate(
    # classification based on never selling
    type_strict = case_when(
      indif2 & indif3   ~ "non",
      dec2 & dec3 & !indif2 & !indif3 ~ "against_women",
      !dec2 & !dec3 & !indif2 & !indif3 ~ "against_men",
      TRUE ~ "mixed"
    ),
    # classification based on 1st decision
    type_1st = case_when(
      indif23_1st==1 ~ "non",
      dec23_1st==1  ~ "against_women",
      !dec23_1st ~ "against_men",
      TRUE ~ "mixed"
    ), 
    # classification based on 2nd decision
    type_2nd = case_when(
      indif23_2nd==1 ~ "non",
      dec23_2nd==1  ~ "against_women",
      !dec23_2nd ~ "against_men",
      TRUE ~ "mixed"
    )
  ) %>% 
  select(-contains("dec23"),
         -contains("indif23"))

# create a long table version with one decision per row  (9 * 240 = 2160 rows)
df_long <- df %>% 
  rename_with(.fn = function(x){paste0(x, "_dec")},
              .cols = contains("dec")) %>% 
  rename_with(.fn = function(x){paste0("dec", str_sub(x,6,6), "_indif")},
              .cols = contains("indif")) %>% 
  pivot_longer(cols = contains("dec"), 
               names_to = c("decision_nr", ".value"),
               names_sep = "_") %>% 
  mutate(decision_nr = as.numeric(str_remove(decision_nr, "dec"))) %>% 
  mutate(chooses_more_qualified = ifelse(decision_nr %in% c(6,7) & dec == 0, 1,
                                         ifelse(decision_nr %in% c(8,9) & dec == 1, 1, 0)),
         male_is_more_qualified = ifelse(decision_nr %in% c(8,9), 1, 0))

# create a long table version with one willingness to pay per row (2 * 240 = 480 rows)
df_wtp <- df %>% 
  pivot_longer(cols = contains("price"), names_to = "cert", values_to = "price") %>% 
  mutate(cert = str_remove(cert, "price_")) %>% 
  mutate(rate = ifelse(cert == "word", scaleword, scaleknow))

#####################################
#### description employer sample ####
#####################################
# table with sample characteristics
tab_sample <- df %>% 
  group_by(treatment) %>% 
  summarise(n = n(),
            age = paste0(format(round(mean(age),1),nsmall=1), 
                         " (", format(round(sd(age),1),nsmall=1), ")"),
            gender_female = paste0(sum(gender=="Female"), 
                                   " (", format(round(mean(gender=="Female")*100,1),nsmall=1), ")"),
            study_stem = paste0(sum(study_coded=="stem",na.rm=TRUE), 
                                " (", format(round(sum(study_coded=="stem",na.rm=TRUE)/n()*100,1),nsmall=1), ")"),
            study_econ = paste0(sum(study_coded=="econ",na.rm=TRUE), 
                                " (", format(round(sum(study_coded=="econ",na.rm=TRUE)/n()*100,1),nsmall=1), ")")) %>% 
  kable(format = "latex")

write(tab_sample, file = "latextables/tab_sample.tex")

#####################################################
#### gender bias in complex and gender decisions ####
#####################################################
# bar chart ultimate choice proportions complex and gender decisions
png("figures/barplot_complex_gender_ult.png", width = 2200, height = 1500, res = 375)
bargraph_choices(df_long %>% filter(decision_nr == 1), 
                 "dec", 
                 "Propensity to hire male", 
                 decisiontype = "ultimate", 
                 sellvar = "indif") + 
  bargraph_choices(df_long %>% filter(decision_nr %in% 2:3), 
                   "dec", 
                   "Propensity to hire male", 
                   decisiontype = "ultimate", 
                   sellvar = "indif") +
  plot_annotation(tag_levels = "A")
dev.off()

# ultimate male choice proportion in complex decision by treatment
df %>% 
  group_by(treatment) %>% 
  summarise(dec1_ultim_male = mean(dec1 & !indif1) + mean(indif1)/2)

# ultimate male choice proportion in complex decision across treatments and mean gender bias
mean_ult_dec1 <- df %>% 
  group_by(treatment) %>% 
  summarise(dec1_ultim_male = mean(dec1 & !indif1) + mean(indif1)/2) %>% 
  summarise(mean(dec1_ultim_male)) %>% pull
(mean_ult_dec1-0.5)*2

pchisq(compute_stat_indep(mean_ult_dec1, 
                          sum(df$treatment=="1"), 
                          sum(df$treatment=="2")),
       df = 1, lower.tail = FALSE)

# ultimate male choice proportion in gender decisions by decision and mean gender bias
mean_ult_dec23 <- df %>% 
  summarise(dec2_ultim_male = mean(dec2 & !indif2) + mean(indif2)/2,
            dec3_ultim_male = mean(dec3 & !indif3) + mean(indif3)/2)
mean((t(mean_ult_dec23)[,1]-0.5)*2)

pchisq(compute_stat_avg(mean_ult_dec23$dec2_ultim_male, nrow(df)),
       df = 1, lower.tail = FALSE)
pchisq(compute_stat_avg(mean_ult_dec23$dec3_ultim_male, nrow(df)),
       df = 1, lower.tail = FALSE)

# test for difference between bias in complex and gender decision
cmh_stat <- map_dfr(1:nrow(df), function(i){
  cont_table_ties(df_long %>% filter(participant == df$participant[i]), 
                  choicevar = "dec",
                  c(1), 
                  c(2,3))}) %>% 
  mutate(treatment = df$treatment) %>% 
  group_by(treatment) %>% 
  mutate(weight = 1/n()) %>%
  ungroup %>% 
  mutate(weight = weight/mean(weight)) %>% 
  summarise(
    CMH = sum(enum_k * weight)^2 / sum(deno_k * weight)
  ) %>% pull
pchisq(cmh_stat, df = 1, lower.tail = FALSE)

#######################################################################
#### types of explicit discrimination, and implicit discrimination ####
#######################################################################
# table with discrimination types by treatment and initial complex decision by type
tab_types1 <- df %>% 
  group_by(treatment, type) %>% 
  summarise(frequency        = n(),
            pr_male_dec1     = mean(dec1),
            .groups = "drop_last") %>% 
  mutate(frequency = frequency/sum(frequency)) %>% 
  ungroup %>% 
  pivot_wider(names_from = treatment, values_from = c(frequency, pr_male_dec1),
              names_prefix = "t")

tab_types2 <- df %>% 
  mutate(type = ifelse(type!="non", "explicit", "non")) %>% 
  group_by(treatment, type) %>% 
  summarise(frequency        = n(),
            pr_male_dec1     = mean(dec1),
            .groups = "drop_last") %>% 
  mutate(frequency = frequency/sum(frequency)) %>% 
  ungroup %>% 
  pivot_wider(names_from = treatment, values_from = c(frequency, pr_male_dec1),
              names_prefix = "t") %>% 
  filter(type == "explicit")

tab_types <- bind_rows(tab_types2, tab_types1) %>% 
  mutate(across(where(is.numeric), ~format(round_half_up(.x*100,1), nsmall = 1))) %>% 
  kable(format = "latex")

write(tab_types, file = "latextables/tab_types.tex")

# test for treatment effect on types
chisq.test(table(df$type, df$treatment), correct = FALSE)

# bounding and testing implicit discrimination against women among explicit anti-men discriminators
df %>% 
  filter(type == "against_men") %>% 
  group_by(treatment) %>% 
  summarise(n = n(),
            p_complex = mean(dec1),
            .groups = "drop") %>%
  summarise(
    lower_bound = p_complex[1] - (1 - p_complex[2]),
    upper_bound = pmin(p_complex[1], p_complex[2]),
    z           = sqrt(compute_stat_indep(mean(p_complex), n[1], n[2])) * sign(lower_bound),
    p           = pnorm(z, lower.tail = FALSE))

# bounding and testing implicit discrimination against women among explicit non-discriminators
df %>% 
  filter(type == "non") %>% 
  group_by(treatment) %>% 
  summarise(n = n(),
            p_complex = mean(dec1),
            .groups = "drop") %>%
  summarise(
    lower_bound = p_complex[1] - (1 - p_complex[2]),
    upper_bound = pmin(p_complex[1], p_complex[2]),
    z           = sqrt(compute_stat_indep(mean(p_complex), n[1], n[2])) * sign(lower_bound),
    p           = pnorm(z, lower.tail = FALSE))

# figure with complex initial and ultimate choices by discrimination type
png("figures/complex_choice_types.png", width = 2200, height = 1400, res = 290)
df %>%
  mutate(
    "italic('Gen'[K]*',')~italic('Gen'[W])" := case_when(
      type == "non" ~ "Explicit:\nnon",
      type == "mixed" ~ "Explicit:\nmixed",
      type == "against_men" ~ "Female",
      TRUE ~ "Male"),
    "italic('Com'[fW]*',')~italic('Com'[fK])~(initial)"  := ifelse(dec1 == 1, "Male", "Female"),
    "italic('Com'[fW]*',')~italic('Com'[fK])~(ultimate)" = ifelse(
      indif1 == 0 & dec1 == 1,
      "Male",
      ifelse(indif1 == 0 & dec1 == 0, "Female", "Sell"))) %>%
  make_long(`italic('Gen'[K]*',')~italic('Gen'[W])`, 
            `italic('Com'[fW]*',')~italic('Com'[fK])~(initial)`, 
            `italic('Com'[fW]*',')~italic('Com'[fK])~(ultimate)`) %>%
  mutate(label = ifelse(
    node == "Male" & x == "italic('Gen'[K]*',')~italic('Gen'[W])", "Explicit:\nagainst women",
    ifelse(node == "Female" &x == "italic('Gen'[K]*',')~italic('Gen'[W])", "Explicit:\nagainst men", node))) %>% 
  mutate(node = factor(node, 
                       ordered = TRUE, 
                       levels = rev(c("Sell", "Male", "Female", "Explicit:\nmixed", "Explicit:\nnon")))) %>% 
  ggplot(aes(x = x, 
             next_x = next_x, 
             node = node, 
             next_node = next_node,
             fill = factor(node),
             label = label)) +
  geom_alluvial(flow.alpha = 0.6) + 
  theme_alluvial(base_size = 14) + 
  geom_alluvial_label(size = 4, color = "black", fill = "white",
                      family = "Segoe UI Semilight") +
  theme(legend.position = "none",
        text = element_text(family = "Segoe UI Semilight")) +
  labs(x = "", y= "N") +
  scale_fill_manual(values = c("grey", "grey", "#fff2ae", "#cbd5e8", "grey" )) +
  annotate("text", x = 1, y = 280, label = "Gender decisions", family = "Segoe UI Semilight", size = 5) +
  annotate("text", x = 2, y = 280, label = "Complex decision", family = "Segoe UI Semilight", size = 5) + 
  geom_segment(aes(x = 1, xend = 1, y = 240, yend = 270), col = "grey20") +
  geom_segment(aes(x = 2, xend = 2, y = 240, yend = 270), col = "grey20") +
  geom_segment(aes(x = 3, xend = 2, y = 240, yend = 270), col = "grey20") +
  scale_x_discrete(labels = function(x) parse(text=x))
dev.off()


##########################
#### simple decisions ####
##########################
# bar chart ultimate choice proportions simple decisions
png("figures/barplot_simple_ult.png", width = 1800, height = 1600, res = 375)
bargraph_choices(df_long %>% filter(decision_nr %in% 6:9), 
                 "chooses_more_qualified", 
                 "Propensity to hire more qualified", 
                 decisiontype = "ultimate", 
                 sellvar = "indif")
dev.off()

# gender bias in simple decisions
mean_ult_dec_simple <- df_long %>% 
  filter(decision_nr %in% 6:9) %>% 
  mutate(certdec = ifelse(decision_nr %in% c(6,8),"simple_know", "simple_word")) %>% 
  group_by(certdec) %>% 
  summarise(dec_ultim_male = mean(dec & !indif) + mean(indif)/2) %>% pull
(mean_ult_dec_simple-0.5)*2

# test for gender bias in simple decision
cmh_stat <- map_dfr(1:nrow(df), function(i){
  cont_table_ties(df_long %>% filter(participant == df$participant[i]), 
                  choicevar = "chooses_more_qualified",
                  c(6,7), 
                  c(8,9))}) %>% 
  summarise(
    CMH = sum(enum_k)^2 / sum(deno_k)
  ) %>% pull
pchisq(cmh_stat, df = 1, lower.tail = FALSE)

##########################
#### redefining merit ####
##########################
# plotting mean and sd of willingness to pay for both certificates by treatment
png("figures/wtp_treatments.png", width = 1600, height = 1400, res = 375)
df_wtp %>% 
  mutate(cert = ifelse(grepl("know", cert), "italic(K)", "italic(W)")) %>% 
  group_by(cert, treatmentlabel) %>% 
  summarise(n = sum(!is.na(price)),
            mean = mean(price, na.rm = TRUE),
            sd = sd(price, na.rm = TRUE), .groups = "drop") %>% 
  mutate(sd_lower = mean-sd,
         sd_upper = mean+sd) %>% 
  ggplot() +
  geom_errorbar(aes(x = treatmentlabel, ymin = sd_lower, ymax = sd_upper, group = cert), 
                width = 0, position = position_dodge(0.2)) +
  geom_point(aes(x = treatmentlabel, shape = cert, y = mean), 
             size = 3, position = position_dodge(0.2)) +
  scale_y_continuous(limits = c(0,100), breaks = seq(0,100,20)) +
  theme_bw(14) +
  theme(panel.grid.minor.x = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.y = element_blank(),
        text = element_text(family = "Segoe UI Semilight"),
        legend.position = "bottom") +
  labs(x = "Treatment",
       y = "WTP (€ cents)",
       shape = "Certificate") + 
  scale_x_discrete(labels = ggplot2:::parse_safe) +
  scale_shape_manual(values = c(17,16), labels = ggplot2:::parse_safe)
dev.off()

# plotting association of elicitation methods
png("figures/association_wtp_rating.png", width = 1600, height = 1400, res = 375)
set.seed(12345)
df_wtp %>% 
  drop_na(price) %>% 
  mutate(likert = ifelse(cert == "word", scaleword, scaleknow)) %>% 
  ggplot() +
  geom_boxplot(aes(y = price, x = factor(likert)), outlier.shape = NA, fill = "grey85") +
  stat_boxplot(aes(y = price, x = factor(likert)), geom = "errorbar", width = 0.2) +
  geom_jitter(aes(y = price, x = factor(likert)), height = 0, width = 0.15, alpha = 0.2) +
  theme_bw(14) +
  theme(panel.grid = element_blank(),
        text = element_text(family = "Segoe UI Semilight")) +
  labs(y = "WTP (€ cents)",
       x = "Informativeness rating")
dev.off()

# regression with switchers excluded
model_excluded <- lm_robust(price ~ treatment*cert, data = df_wtp, 
                            clusters = participant, se_type = "stata")

# regression with switchers imputed
pred_matrix <- matrix(0, nrow = ncol(df_wtp), ncol = ncol(df_wtp))
pred_matrix[which(names(df_wtp)=="price"), which(names(df_wtp)=="rate")] <- 1

set.seed(12345)
df_wtp_imp <- mice(df_wtp,
                   m = 100,
                   method = "pmm",
                   maxit = 1,
                   print = FALSE,
                   predictorMatrix = pred_matrix)

mean_imputed <- apply(df_wtp_imp$imp$price, 1, mean)
rated <- df_wtp$rate[is.na(df_wtp$price)]
plot(rated, mean_imputed)

models_mi <- with(df_wtp_imp, 
                  lm_robust(price ~ treatment*cert,
                            clusters = participant, se_type = "stata"))

model_imputed <- pool(models_mi)

# regression separately by discrimination type
models_type <- map(as.list(unique(df$type)), function(x){
  lm_robust(price ~ treatment*cert, data = df_wtp %>% filter(type == x, !is.na(price)), 
            clusters = participant, se_type = "stata")
})
names(models_type) <- unique(df$type)

# regression table
tab_models <- modelsummary(
  list(
    "Multiple switchers excluded" = model_excluded,
    "Multiple switchers imputed"  = model_imputed,
    "Explicit: against men"       = models_type$against_men,
    "Explicit: against women"     = models_type$against_women,
    "Explicit: mixed"             = models_type$mixed,
    "Explicit: none"              = models_type$non),
  fmt = 1,
  stars = c("*" = 0.1, "**" = 0.05, "***" = 0.01),
  coef_rename = c("treatment2" = "T2",
                  "certword" = "Word",
                  "treatment2:certword" = "T2:Word"),
  gof_omit = "dj", output = "latex") %>% 
  add_header_above(c(" " = 1,
                     "Full sample" = 2,
                     "By discrimination types (Multiple switchers excluded)" = 4))

write(tab_models, file = "latextables/tab_models.tex")

################################################
#### statistical accuracy of discrimination ####
################################################
# plot smoothed density of job task performance by gender
png("figures/job_performance_gender.png", width = 1600, height = 1400, res = 375)
ggplot(df_candidates) +
  geom_density(aes(x = matrices, linetype = gender), key_glyph = draw_key_path) +
  theme_bw(14) +
  theme(panel.grid = element_blank(),
        text = element_text(family = "Segoe UI Semilight"),
        legend.position = "bottom") +
  guides(linetype = guide_legend(keywidth = 2)) +
  labs(y = "Density",
       x = "Job task performance",
       linetype = "Gender")
dev.off()

# table performance distribution in job task between genders
tab_performance <- df_candidates %>% 
  group_by(gender) %>% 
  summarise(
    n = n(),
    across(matrices, .fns = list(
      mean = mean,
      sd = sd,
      min = min,
      p25 = ~quantile(.x, 0.25),
      median = median,
      p75 = ~quantile(.x, 0.25),
      max = max
    ))
  ) %>% 
  pivot_longer(cols = !contains("gender"),
               names_to = "statistics",
               values_to = "val") %>% 
  pivot_wider(names_from = gender, values_from = val) %>% 
  mutate(across(where(is.numeric), ~format(round_half_up(.x, 2), nsmall = 2))) %>% 
  kable(format = "latex")

write(tab_performance, file = "latextables/tab_performance.tex")

# test gender difference in performance
t.test(matrices ~ gender, data = df_candidates, var.equal = TRUE)

# test first-order beliefs about gender against neutral benchmark
with(df_candidates, t.test(estimate_matrices, mu = 50))

# test second-order beliefs about gender against neutral benchmark
with(df_candidates, t.test(belief_matrices, mu = 50))

# plot beliefs by gender
png("figures/distribution_stereotype.png", width = 1600, height = 1400, res = 375)
set.seed(12345)
df_candidates %>% 
  pivot_longer(cols = c(estimate_matrices, belief_matrices),
               names_to = "var", values_to = "val") %>% 
  mutate(var = ifelse(grepl("est", var), "Own belief", "Others' belief")) %>% 
  mutate(var = factor(var, ordered = TRUE, levels = c("Own belief",
                                                      "Others' belief"))) %>% 
  ggplot(aes(x = var, y = val)) +
  geom_boxplot(outlier.shape = NA, fill = "grey85") +
  stat_boxplot(geom = "errorbar", width = 0.2) +
  geom_jitter(height = 0, width = 0.05, alpha = 0.2) +
  geom_hline(yintercept = 50, linetype = 2) +
  theme_bw(14) +
  theme(panel.grid.minor.x = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid.minor.y = element_blank(),
        text = element_text(family = "Segoe UI Semilight")) +
  scale_y_continuous(limits = c(0,100), breaks = seq(0,100,20)) +
  labs(x = "",
       y = "Random pairings in which\nmale outperforms female")
dev.off()

# table observed probability of superior performance conditional on compared profiles
pairedcomp <- function(x,y){
  comb.grid <- expand.grid(x,y)
  a  <- sum(comb.grid[,1] > comb.grid[,2]) / nrow(comb.grid)
  b  <- sum(comb.grid[,1] < comb.grid[,2]) / nrow(comb.grid)
  tie <- sum(comb.grid[,1] == comb.grid[,2]) / nrow(comb.grid)
  
  return(data.frame(
    proportion = c(a, b, tie),
    outcome = c("a", "b", "tie")
  ))}

p70_w <- quantile(df_candidates$wordpuzzles, 0.7)
p70_k <- quantile(df_candidates$generalknowledge, 0.7)

n_certified <- nrow(df_candidates) * 0.3
n_tied_w    <- sum(df_candidates$wordpuzzles == p70_w)
n_nontied_w <- sum(df_candidates$wordpuzzles > p70_w)
n_tied_k    <- sum(df_candidates$generalknowledge == p70_k)
n_nontied_k <- sum(df_candidates$generalknowledge > p70_k)

comb_w <- combn(1:n_tied_w, n_certified-n_nontied_w, simplify = FALSE)
comb_k <- combn(1:n_tied_k, n_certified-n_nontied_k, simplify = FALSE)

possible_datasets_w <- map(comb_w, function(x){
  nontied_df <- df_candidates %>% 
    filter(wordpuzzles > p70_w)
  tied_df <- df_candidates %>% 
    filter(wordpuzzles == p70_w) %>% 
    {.[x,]}
  rbind(nontied_df, tied_df) %>% as_tibble
})

possible_datasets_k <- map(comb_k, function(x){
  nontied_df <- df_candidates %>% 
    filter(generalknowledge > p70_k)
  tied_df <- df_candidates %>% 
    filter(generalknowledge == p70_k) %>% 
    {.[x,]}
  rbind(nontied_df, tied_df) %>% as_tibble
})

comb_w_k <- expand_grid(nr_dataset_w = 1:length(comb_w), nr_dataset_k = 1:length(comb_k))

results_all_datasets <- map_dfr(1:nrow(comb_w_k), function(x){

  dataset_nrs <- comb_w_k[x,]
  dataset_w <- possible_datasets_w[[as.numeric(dataset_nrs[1])]]
  dataset_k <- possible_datasets_k[[as.numeric(dataset_nrs[2])]]
  
  performances <- list(
    `fW` = dataset_w$matrices[dataset_w$gender=="Female"],
    `fK` = dataset_k$matrices[dataset_k$gender=="Female"],
    `mW` = dataset_w$matrices[dataset_w$gender=="Male"],
    `mK` = dataset_k$matrices[dataset_k$gender=="Male"],
    `f_` = df_candidates$matrices[df_candidates$gender=="Female"],
    `m_` = df_candidates$matrices[df_candidates$gender=="Male"],
    `K_` = dataset_k$matrices,
    `W_` = dataset_w$matrices,
    `no` = df_candidates$matrices
  )
  
  collected_results <- data.frame(
    decision   = c("D1 (T1)", "D1 (T2)", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", rep("n.a.", 4)),
    candidate_a = c("fW", "fK", "fK", "fW", "fW", "mW", "fK", "fW", "f_", "f_","K_","K_", "W_", "f_"),
    candidate_b = c("mK", "mW", "mK", "mW", "fK", "mK", "m_", "m_", "mK", "mW", "W_", "no", "no", "m_")
  )
  
  collected_results$tie <-  collected_results$pr_b_better <- collected_results$pr_a_better <- numeric(nrow(collected_results))
  
  for (i in 1:nrow(collected_results)){

    prop_comp <- pairedcomp(with(performances, eval(parse(text = collected_results$candidate_a[i]))),
                            with(performances, eval(parse(text = collected_results$candidate_b[i]))))
    
    collected_results$pr_a_better[i] <- prop_comp[1,1]
    collected_results$pr_b_better[i] <- prop_comp[2,1]
    collected_results$tie[i]         <- prop_comp[3,1]
  }
  
  collected_results$pr_a_better <-  collected_results$pr_a_better +  collected_results$tie/2
  collected_results$pr_b_better <-  collected_results$pr_b_better +  collected_results$tie/2
  
  return(collected_results)
})

tab_winning <- results_all_datasets %>% 
  group_by(decision, candidate_a, candidate_b) %>% 
  summarise(across(where(is.numeric), ~format(round_half_up(mean(.x), 3), nsmall=3)), 
            .groups = "drop") %>% 
  kable(format = "latex")

write(tab_winning, file = "latextables/tab_winning.tex")

#################################
#### role of employer gender ####
#################################
# propensity to hire male candidate across the seven male-vs-female decisions by employer gender
df_long %>%
  filter(!decision_nr %in% c(4:5)) %>% 
  tabyl(
    gender, dec
  ) %>% 
  adorn_percentages()

############################
#### robustness results ####
############################
# ultimate male choice proportion in complex decision by treatment and explicit discrimination types
tab_types1_ult <- df %>% 
  group_by(treatment, type) %>% 
  summarise(frequency        = n(),
            pr_male_dec1_ult = mean(dec1 & !indif1) + mean(indif1)/2,
            .groups = "drop_last") %>% 
  mutate(frequency = frequency/sum(frequency)) %>% 
  ungroup %>% 
  pivot_wider(names_from = treatment, values_from = c(frequency, pr_male_dec1_ult),
              names_prefix = "t")
tab_types1_ult

# mean gender bias in complex decision by treatment among explicit gender discriminators
mean_ult_dec1_types <- df %>% 
  group_by(type, treatment) %>% 
  summarise(dec1_ultim_male = mean(dec1 & !indif1) + mean(indif1)/2,
            .groups = "drop_last") %>% 
  filter(grepl("against", type)) %>% 
  summarise(mean(dec1_ultim_male)) %>% pull
(mean_ult_dec1_types-0.5)*2

# analyze implicit discrimination when counting ultimate choices as if they were initial
df %>% 
  filter(type == "against_men") %>% 
  group_by(treatment) %>% 
  summarise(n = n(),
            p_complex = mean(dec1 & !indif1) + mean(indif1)/2,
            .groups = "drop") %>%
  summarise(
    lower_bound = p_complex[1] - (1 - p_complex[2]),
    upper_bound = pmin(p_complex[1], p_complex[2]),
    z           = sqrt(compute_stat_indep(mean(p_complex), n[1], n[2])) * sign(lower_bound),
    p           = pnorm(z, lower.tail = FALSE))

# analyze implicit discrimination for alternative type definitions
definitions <- c("type", "type_strict", "type_1st", "type_2nd")
names(definitions) <- definitions

tab_implicitalternatives <- map_dfr(definitions, .id = "definition", function(x){

  df %>% 
    filter(!!as.symbol(x) == "against_men") %>% 
    group_by(treatment) %>% 
    summarise(n = n(),
              p_complex = mean(dec1),
              .groups = "drop")
  
  }) %>% 
  group_by(definition) %>% 
  summarise(
    lower_bound = p_complex[1] - (1 - p_complex[2]),
    upper_bound = pmin(p_complex[1], p_complex[2]),
    z           = sqrt(compute_stat_indep(mean(p_complex), n[1], n[2])) * sign(lower_bound),
    p           = pnorm(z, lower.tail = FALSE)
  ) %>% 
  mutate(across(contains("bound"), ~format(round_half_up(.x * 100, 1), nsmall = 1))) %>% 
  kable(format = "latex", booktabs = TRUE, linesep = "", digits = 3)

write(tab_implicitalternatives, file = "latextables/tab_implicitalternatives.tex")

# analyze implicit discrimination against other attributes
implicit_against <- c("Female gender", "Male gender", "Word certificate", "Knowledge certificate")

tab_implicitattributes <- map_dfr(implicit_against, function(x){
  
  if (x == "Female gender"){
    explicit_pref <- "against_men"
    implicit_count <- "dec1"
  }
  if (x == "Male gender"){
    explicit_pref <- "against_women"
    implicit_count <- "!dec1"
  }
  if (x == "Word certificate"){
    explicit_pref <- "against_know"
    implicit_count <- "(dec1 & treatment == '1') | (!dec1 & treatment == '2')"
  }
  if (x == "Knowledge certificate"){
    explicit_pref <- "against_word"
    implicit_count <- "(dec1 & treatment == '2') | (!dec1 & treatment == '1')"
  }
  
  df %>% 
    filter(type == explicit_pref | type_cert == explicit_pref) %>% 
    group_by(treatment) %>% 
    summarise(n = n(),
              p_complex = mean(eval(parse(text = implicit_count))),
              .groups = "drop") %>%
    summarise(
      attribute   = x,
      lower_bound = p_complex[1] - (1 - p_complex[2]),
      upper_bound = pmin(p_complex[1], p_complex[2]),
      z           = sqrt(compute_stat_indep(mean(p_complex), n[1], n[2])) * sign(lower_bound),
      p           = pnorm(z, lower.tail = FALSE))
}) %>% 
  mutate(across(contains("bound"), ~format(round_half_up(.x * 100, 1), nsmall = 1))) %>% 
  kable(format = "latex", booktabs = TRUE, linesep = "", digits = 3)

write(tab_implicitattributes, file = "latextables/tab_implicitattributes.tex")
