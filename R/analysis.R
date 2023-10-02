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

# create column that classifies for explicit discrimination type
df <- df %>% 
  mutate(type = case_when(
    indif2 & indif3 ~ "non",
    dec2 & dec3     ~ "against_women",
    !dec2 & !dec3   ~ "against_men",
    TRUE            ~ "mixed"
  ))

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