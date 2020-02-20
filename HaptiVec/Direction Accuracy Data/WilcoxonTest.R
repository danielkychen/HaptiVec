##Script for HaptVec Wilcoxon Signed Rank Test

NL <- c(100, 90, 100, 90, 30, 100, 100, 90, 90, 100);
NW <- c(100, 40, 100, 80, 60, 100, 90, 100, 100, 100);
W <- c(90, 40, 70, 100, 50, 100, 80, 100, 100, 90);
SW <- c(100, 80, 60, 80, 80, 100, 100, 100, 100, 100);
SL <- c(80, 90, 80, 100, 100, 100, 100, 90, 100, 100);
SR <- c(100, 100, 100, 100, 100, 100, 70, 60, 90, 100);
SE <- c(100, 40, 50, 100, 100, 90, 100, 80, 30, 100);
E <- c(80, 40, 100, 100, 90, 100, 60, 100, 80, 60);
NE <- c(100, 50, 90, 90, 70, 100, 100, 100, 90, 100);
NR <- c(100, 90, 80, 70, 50, 100, 100, 100, 100, 100);

wilcox.test(NL, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(NL, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(NW, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(NW, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(W, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(W, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(SW, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(SW, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(SL, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(SL, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(SR, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(SR, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(SE, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(SE, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(E, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(E, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(NE, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(NE, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)

wilcox.test(NR, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)
qnorm(wilcox.test(NR, y = NULL, alternative = "greater", mu = 20, paired = FALSE, exact = FALSE)$p.value)
