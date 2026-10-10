# راهنمای جامع آنالیز داده‌های Real-Time PCR (Excel, R و نرم‌افزارهای تخصصی)

---

## ۱. روش‌های فرمولی محاسبات کمی سنجش بیان ژن

### ۱.۱. روش کمی نسبی $2^{-\Delta \Delta C_t}$ (Livak Method)
شرط اصلی استفاده از این روش، **یکسان بودن راندمان تکثیر (Amplification Efficiency) ژن هدف و ژن مرجع (Housekeeping Gene)** است (راندمان بین ۹۰٪ تا ۱۱۰٪).

$$\Delta C_t (\text{نمونه}) = C_t (\text{Target}) - C_t (\text{Housekeeping})$$
$$\Delta \Delta C_t = \Delta C_t (\text{Case}) - \Delta C_t (\text{Control})$$
$$\text{Fold Change} = 2^{-\Delta \Delta C_t}$$

---

## ۲. آنالیز داده‌ها در Microsoft Excel (گام به گام)

1. **تنظیم ستون‌ها:**
   * ستون A: Sample Name | ستون B: Target Gene $C_t$ | ستون C: Housekeeping $C_t$
2. **محاسبه $\Delta C_t$:** در خانه D2 فرمول `=B2-C2` را وارد کنید.
3. **محاسبه میانگین $\Delta C_t$ برای گروه کنترل:** (فرضاً سلول‌های E2 تا E4).
4. **محاسبه $\Delta \Delta C_t$:** در خانه F2 فرمول `=D2-$E$2` را بنویسید.
5. **محاسبه تغییر بیان (Fold Change):** در خانه G2 فرمول `=POWER(2, -F2)` را درج کنید.

---

## ۳. کدنویسی و آنالیز اتوماتیک در زبان R

برای آنالیز و رسم نمودارهای استاندارد مقاله در R می‌توانید از پکیج‌های `tidyverse` و `pcr` استفاده کنید:

```R
# نصب و فراخوانی پکیج‌های مورد نیاز
install.packages("pcr")
library(pcr)
library(tidyverse)

# وارد کردن فایل داده‌ها (حاوی مقادیر Ct)
ct_data <- read_csv("qpcr_data.csv")

# محاسبه بیان نسبی به روش Livak
res <- pcr_calc_expression(
  df = ct_data,
  group_var = "group",
  reference_gene = "GAPDH",
  target_gene = "TNF_alpha",
  method = "delta_delta_ct"
)

# رسم نمودار ستونی کیفیت بالا با ggplot2
ggplot(res, aes(x = group, y = relative_expression, fill = group)) +
  geom_bar(stat = "identity", width = 0.5, position = "dodge") +
  geom_errorbar(aes(ymin = relative_expression - sd, ymax = relative_expression + sd), width = 0.2) +
  theme_classic() +
  labs(title = "Fold Change of TNF-alpha Gene Expression", y = "Relative Expression (2^-ddCt)")