# function for plotting bar graphs of choice proportions
bargraph_choices <- function(data, 
                             choicevar, 
                             ylab, 
                             decisiontype, # 'initial', 'ultimate', 'both' 
                             sellvar = NULL){
  
  # define informative decision labels in plotmath language
  labels <- tribble(
    ~decision_nr, ~treatment, ~label,
    1, "1", "italic('Com'[fW])",
    1, "2", "italic('Com'[fK])",
    2, "1", "italic('Gen'[K])", 
    2, "2", "italic('Gen'[K])", 
    3, "1", "italic('Gen'[W])", 
    3, "2", "italic('Gen'[W])", 
    4, "1", "italic('Cer'[f])", 
    4, "2", "italic('Cer'[f])", 
    5, "1", "italic('Cer'[m])", 
    5, "2", "italic('Cer'[m])", 
    6, "1", "italic('Sim'[fK])",
    6, "2", "italic('Sim'[fK])",
    7, "1", "italic('Sim'[fW])", 
    7, "2", "italic('Sim'[fW])", 
    8, "1", "italic('Sim'[mK])", 
    8, "2", "italic('Sim'[mK])", 
    9, "1", "italic('Sim'[mW])", 
    9, "2", "italic('Sim'[mW])"
  )
  
  data <- data %>% 
    left_join(labels, by = c("decision_nr", "treatment")) %>% 
    mutate(order = as.numeric(paste0(decision_nr, treatment)),
           label = fct_reorder(factor(label), order, mean))
  
  # calculate proportions
  if(decisiontype == "initial"){
    plotdata <- data %>%
      group_by(label) %>% 
      summarise(
        #initial
        ratio_hire    = paste0(sum(!!as.symbol(choicevar)), "/", n()),
        mean_hire     = mean(!!as.symbol(choicevar)),
        ci_lower      = binom.confint(sum(!!as.symbol(choicevar)), n(), methods = "wilson")$lower,
        ci_upper      = binom.confint(sum(!!as.symbol(choicevar)), n(), methods = "wilson")$upper
      )
  } else if(decisiontype == "both"){
    plotdata <- data %>%
      group_by(label) %>% 
      summarise(
        #initial
        ratio_hire    = paste0(sum(!!as.symbol(choicevar)), "/", n()),
        mean_hire     = mean(!!as.symbol(choicevar)),
        ci_lower      = binom.confint(sum(!!as.symbol(choicevar)), n(), methods = "wilson")$lower,
        ci_upper      = binom.confint(sum(!!as.symbol(choicevar)), n(), methods = "wilson")$upper,
        # ultimate
        mean_hire_ult = mean(!!as.symbol(choicevar) & !!as.symbol(sellvar)==0) + mean(!!as.symbol(sellvar)==1)/2,
        ci_lower_ult  = binom.confint(sum(!!as.symbol(choicevar) & !!as.symbol(sellvar)==0) + sum(!!as.symbol(sellvar)==1)/2, n(), methods = "wilson")$lower,
        ci_upper_ult  = binom.confint(sum(!!as.symbol(choicevar) & !!as.symbol(sellvar)==0) + sum(!!as.symbol(sellvar)==1)/2, n(), methods = "wilson")$upper
      )
    plotdata_long <- plotdata %>% 
      select(-ratio_hire) %>% 
      pivot_longer(where(is.numeric), names_to = "var", values_to = "val") %>% 
      mutate(ult = ifelse(grepl("ult", var), "ultimate", "initial"),
             var = str_remove(var, "_ult")) %>% 
      pivot_wider(names_from = var, values_from = val)
  } else if(decisiontype == "ultimate"){
    plotdata <- data %>%
      group_by(label) %>% 
      summarise(
        #ultimate
        mean_hire_ult = mean(!!as.symbol(choicevar) & !!as.symbol(sellvar)==0) + mean(!!as.symbol(sellvar)==1)/2,
        ci_lower_ult  = binom.confint(sum(!!as.symbol(choicevar) & !!as.symbol(sellvar)==0) + sum(!!as.symbol(sellvar)==1)/2, n(), methods = "wilson")$lower,
        ci_upper_ult  = binom.confint(sum(!!as.symbol(choicevar) & !!as.symbol(sellvar)==0) + sum(!!as.symbol(sellvar)==1)/2, n(), methods = "wilson")$upper
      )
  }
  
  # initiate plot
  p <-
    ggplot() + 
    scale_y_continuous(breaks = seq(0,1,0.2), limits = c(0,1)) +
    theme_minimal(14) +
    theme(panel.grid.minor.x = element_blank(),
          panel.grid.major.x = element_blank(),
          axis.title.y = element_markdown(),
          legend.position = "bottom",
          text = element_text(family = "Segoe UI Semilight"))
  
  # add bars
  if(decisiontype == "initial"){
    p <- p + 
      geom_bar(data = plotdata,
               aes(x = label, y = mean_hire),
               stat = "identity", col = "black", fill = "grey85") +
      geom_hline(yintercept = 0.5, linetype = 2, lwd = 1/3) +
      geom_errorbar(data = plotdata,
                    aes(x = label, ymin = ci_lower, ymax = ci_upper),
                    width = 0.25) +
      geom_text(data = plotdata,
                aes(x = label, y = 0.03, label = ratio_hire), 
                size = 4, family = "Segoe UI Semilight") + 
      scale_x_discrete(labels = ggplot2:::parse_safe) +
      labs(y = ylab,
           x = "Decision")
    
  } else if(decisiontype == "both"){
    p <- p + 
      geom_bar(data = plotdata_long,
               aes(x = label, y = mean_hire, fill = ult),
               stat = "identity", col = "black", position = position_dodge(width=0.9)) +
      geom_hline(yintercept = 0.5, linetype = 2, lwd = 1/3) +
      geom_errorbar(data = plotdata_long,
                    aes(x = label, ymin = ci_lower, ymax = ci_upper, group = ult),
                    width = 0.25, position = position_dodge(width=0.9)) +
      geom_text(data = plotdata_long,
                aes(x = label, y = 0.03, label = paste0(format(round_half_up(mean_hire*100,1), nsmall=1),"%"), group = ult), 
                size = 4, family = "Segoe UI Semilight", position = position_dodge(width=0.9)) + 
      scale_fill_manual(values = c("grey85", "#a6cee3")) + 
      scale_x_discrete(labels = ggplot2:::parse_safe) +
      labs(y = ylab,
           fill = "",
           x = "Decision")
  } else if(decisiontype == "ultimate")
    p <- p + 
    geom_bar(data = plotdata,
             aes(x = label, y = mean_hire_ult),
             stat = "identity", col = "black", fill = "grey85") +
    geom_hline(yintercept = 0.5, linetype = 2, lwd = 1/3) +
    geom_errorbar(data = plotdata,
                  aes(x = label, ymin = ci_lower_ult, ymax = ci_upper_ult),
                  width = 0.25) +
    geom_text(data = plotdata,
              aes(x = label, y = 0.03, label = paste0(format(round_half_up(mean_hire_ult*100,1), nsmall=1),"%")), 
              size = 4, family = "Segoe UI Semilight") + 
    scale_x_discrete(labels = ggplot2:::parse_safe) +
    labs(y = ylab,
         x = "Decision")
  return(p)
}

# function to compute score test statistic from fraction and sample size for null
# hypothesis that fraction = 0.5 when only fraction and sample size is given
compute_stat_avg <- function(avg_frac, n){
  ((avg_frac-0.5) / sqrt(0.5^2/n))^2
}

# function to compute score test statistic from fraction and sample sizes for null hypothesis
# that fraction = 0.5 when fraction is itself the average of two independent fractions
compute_stat_indep <- function(avg_frac, n1, n2){
  ((avg_frac-0.5) / sqrt((0.5^2/n1 + 0.5^2/n2)/4))^2
}

# function to compute cochran-mantel-haenszel statistic under the presence of 
# ties due to selling the choice
cont_table_ties <- function(data, choicevar = "dec", decision_nrs_A, decision_nrs_B){
  
  data[,"dec"] <- data[,choicevar]
  data$dec     <- factor(data$dec, levels = c(0,1))
  data$indif   <- factor(data$indif, levels = c(0,1))
  decsA        <- data %>% filter(decision_nr %in% decision_nrs_A)
  decsB        <- data %>% filter(decision_nr %in% decision_nrs_B)
  
  # create a contingency table which counts ties as half
  non_sellers_A <- as.matrix(t(table(decsA$dec[decsA$indif==0])))
  non_sellers_B <- as.matrix(t(table(decsB$dec[decsB$indif==0])))
  
  selling_A <- sum(decsA$indif==1)
  selling_B <- sum(decsB$indif==1)
  
  cont_matr <- rbind(non_sellers_A + selling_A * 0.5,
                     non_sellers_B + selling_B * 0.5)
  
  # compute contributions to test statistic from it
  cont_matr_margins <- addmargins(cont_matr)
  n11 <- cont_matr_margins[1,1]
  n1_ <- cont_matr_margins[1,3]
  n2_ <- cont_matr_margins[2,3]
  n_1 <- cont_matr_margins[3,1]
  n_2 <- cont_matr_margins[3,2]
  n__ <- cont_matr_margins[3,3]
  
  enum_k = n11 - n1_ * n_1 / n__
  deno_k = n1_ * n2_ * n_1 * n_2 / (n__^2 * (n__-1)) 
  
  return(tibble(enum_k = enum_k,
                deno_k = deno_k))
}
