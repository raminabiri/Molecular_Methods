# پروتکل‌های دقیق، ریز به ریز و گام‌به‌گام آزمایشگاهی

<details>
<summary><b>پروتکل ۱: آماده‌سازی و استخراج DNA با خلوص بالا</b></summary>

> **نکته بسیار حیاتی:** کیفیت و غلظت DNA ورودی در RAPD و AFLP تعیین‌کننده اصلی تکرارپذیری است ($A_{260}/A_{280} = 1.8 - 2.0$).

1. استخراج DNA ژنومی با استفاده از کیت‌های ستونی silica-based جهت خروج کامل نمک‌ها و مهارکننده‌ها.
2. سنجش غلظت با دستگاه NanoDrop و تنظیم غلظت نهایی روی **$10-20 \text{ ng/}\mu\text{L}$**.

</details>

<details>
<summary><b>پروتکل ۲: اجرای کامل RAPD-PCR</b></summary>

### ۱. مسترمیکس واکنش RAPD (حجم نهایی $25 \mu\text{L}$)
* $12.5 \mu\text{L}$ بافر 2X PCR Master Mix (یا Taq DNA Polymerase به همراه $1.5 \text{ mM } MgCl_2$)
* $1.0 \mu\text{L}$ پرایمر ۱۰-مر تک (مثلاً OPA-02 با غلظت $10 \mu\text{M}$)
* $2.0 \mu\text{L}$ DNA الگوی استخراج‌شده ($20 \text{ ng}$)
* $9.5 \mu\text{L}$ آب nuclease-free

### ۲. برنامه ترموسایکلر RAPD
* **دناتوراسیون اولیه:** $94^\circ\text{C}$ به مدت ۵ دقیقه
* **۴۰ سیکل شامل:**
  * دناتوراسیون: $94^\circ\text{C}$ به مدت ۱ دقیقه
  * **اتصال پرایمر (Annealing):** **$36^\circ\text{C}$ به مدت ۱ دقیقه** (بسیار حیاتی)
  * بسط (Extension): $72^\circ\text{C}$ به مدت ۲ دقیقه
* **بسط نهایی:** $72^\circ\text{C}$ به مدت ۱۰ دقیقه

</details>

<details>
<summary><b>پروتکل ۳: اجرای کامل ERIC-PCR و REP-PCR</b></summary>

### ۱. مخلوط واکنش ERIC-PCR ($25 \mu\text{L}$)
* $12.5 \mu\text{L}$ بافر 2X Taq Master Mix
* $1.0 \mu\text{L}$ پرایمر ERIC1R ($10 \mu\text{M}$)
* $1.0 \mu\text{L}$ پرایمر ERIC2 ($10 \mu\text{M}$)
* $2.0 \mu\text{L}$ DNA الگو ($30-50 \text{ ng}$)
* $8.5 \mu\text{L}$ آب nuclease-free

### ۲. برنامه ترموسایکلر ERIC-PCR
* **دناتوراسیون اولیه:** $95^\circ\text{C}$ به مدت ۷ دقیقه
* **۳۵ سیکل شامل:**
  * $94^\circ\text{C}$ به مدت ۱ دقیقه
  * **$52^\circ\text{C}$ به مدت ۱ دقیقه**
  * $65^\circ\text{C}$ به مدت ۸ دقیقه (زمان بسط طولانی جهت تکثیر قطعات بزرگ)
* **بسط نهایی:** $65^\circ\text{C}$ به مدت ۱۶ دقیقه

</details>

<details>
<summary><b>پروتکل ۴: اجرای گام‌به‌گام و ریز تکنیک AFLP</b></summary>

### گام ۱: هضم آنزیمی دوگانه و اتصال آداپتور (Restriction-Ligation)
* $250 \text{ ng}$ DNA ژنومی
* $5 \text{ U}$ آنزیم *EcoRI* + $5 \text{ U}$ آنزیم *MseI*
* $1 \mu\text{L}$ آداپتور EcoRI + $1 \mu\text{L}$ آداپتور MseI
* $1 \text{ U}$ آنزیم T4 DNA Ligase + بافر اختصاصی 10X
* انکوباسیون در دمای $37^\circ\text{C}$ به مدت ۲ ساعت.

### گام ۲: پیش‌تکثیر (Pre-selective Amplification)
* $2.5 \mu\text{L}$ از محصول هضم‌شده رقیق‌شده (۱:۱۰)
* $1 \mu\text{L}$ پرایمر EcoRI+A + $1 \mu\text{L}$ پرایمر MseI+C
* $10 \mu\text{L}$ PCR Master Mix
* برنامه PCR: ۲۰ سیکل ($94^\circ\text{C}$ 30s, $56^\circ\text{C}$ 30s, $72^\circ\text{C}$ 60s).

### گام ۳: تکثیر انتخابی (Selective Amplification)
* $2.5 \mu\text{L}$ از محصول پیش‌تکثیر رقیق‌شده (۱:۲۰)
* $1 \mu\text{L}$ پرایمر EcoRI+AAC (فلورسنت لیبل‌شده) + $1 \mu\text{L}$ پرایمر MseI+CAG
* برنامه PCR با روش Touchdown: شروغ اتصال از $65^\circ\text{C}$ و کاهش ۰.۷ درجه در هر سیکل به مدت ۱۲ سیکل، سپس ۲۳ سیکل در $56^\circ\text{C}$.

</details>

<details>
<summary><b>پروتکل ۵: الکتروفورز، آنالیز و رسم دندروگرام</b></summary>

1. **الکتروفورز:**
   * برای RAPD و ERIC/REP: ژل آگارز ۱.۵٪ تا ۲٪ در بافر 1X TAE، ولتاژ $4 \text{ V/cm}$ به مدت ۳ تا ۴ ساعت.
   * برای AFLP: الکتروفورز مویین دستگاه کاپیلری سکوئنسر (مثل ABI 3500) یا ژل پلی‌آکریل‌آمید ۶٪ (PAGE).
2. **آنالیز داده‌ها:**
   * تشکیل ماتریس باینری صفر و یک ($1 = \text{Presence}$, $0 = \text{Absence}$).
   * محاسبه ضریب تشابه (Dice or Jaccard Coefficient).
   * رسم دندروگرام درخت خویشاوندی با الگوریتم **UPGMA** یا Neighbor-Joining در نرم‌افزارهای GelJ یا BioNumerics.

</details>