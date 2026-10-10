# پروتکل‌های صفر تا صد آزمایشگاهی و عملیاتی MLST

<details>
<summary><b>مرحله ۱: استخراج DNA ژنومی باکتری (gDNA Extraction)</b></summary>

1. کشت باکتری در محیط TSA یا LB به مدت ۱۶-۲۴ ساعت در $37^\circ\text{C}$.
2. برداشتن ۲-۳ کلونی تک و حل کردن در $100 \mu\text{L}$ آب nuclease-free یا بافر TE.
3. **روش جوشاندن (Boiling) برای گرم‌منفی‌ها:**
   * قرار دادن لوله در بن‌ماری یا ترموبلاک $100^\circ\text{C}$ به مدت ۱۰ دقیقه.
   * سانتریفیوژ در $12000 \text{ rpm}$ به مدت ۵ دقیقه.
   * برداشتن روئیت (حاوی DNA) و انتقال به لوله تازه.
4. **استفاده از کیت استخراج ستونی (برای گرم‌مثبت‌ها):** استفاده از آنزیم‌های لیزوزیم/لیزوستافین قبل از لیز سلولی جهت شکستن دیواره سلولی.
5. سنجش غلظت و خلوص DNA با دستگاه نانودراپ (نسبت $A_{260}/A_{280}$ بین ۱.۸ تا ۲.۰).

</details>

<details>
<summary><b>مرحله ۲: طراحی و آماده‌سازی واکنش PCR برای ۷ ژن خانه‌دار</b></summary>

> **مثال طراح استاندارد برای باکتری *Klebsiella pneumoniae* (۷ ژن: *gapA, infB, mdh, pgi, phoE, rpoB, tonB*):**

### ۱. فرمولاسیون مسترمیکس PCR (برای یک واکنش $25 \mu\text{L}$):
* 2X PCR Master Mix (حاوی Taq Polymerase, dNTPs, Buffer): $12.5 \mu\text{L}$
* پرایمر رفت (Forward Primer - $10 \mu\text{M}$): $1.0 \mu\text{L}$
* پرایمر برگشت (Reverse Primer - $10 \mu\text{M}$): $1.0 \mu\text{L}$
* DNA الگوی الگو ($20-50 \text{ ng/\mu L}$): $2.0 \mu\text{L}$
* آب مقطر استریل (Nuclease-free water): $8.5 \mu\text{L}$
* **حجم کل:** $25 \mu\text{L}$

### ۲. برنامه ترموسایکلر (PCR Program Standard):
1. **دناتوراسیون اولیه:** $95^\circ\text{C}$ به مدت ۵ دقیقه
2. **۳۵ سیکل شامل:**
   * دناتوراسیون: $94^\circ\text{C}$ به مدت ۳۰ ثانیه
   * اتصال پرایمر (Annealing): **$55^\circ\text{C} - 58^\circ\text{C}$** (بسته به ژن) به مدت ۳۰ ثانیه
   * بسط (Extension): $72^\circ\text{C}$ به مدت ۱ دقیقه
3. **بسط نهایی:** $72^\circ\text{C}$ به مدت ۵ دقیقه
4. نگهداری در $4^\circ\text{C}$.

</details>

<details>
<summary><b>مرحله ۳: تایید محصولات PCR و خالص‌سازی (Purification)</b></summary>

1. **الکتروفورز تاییدی:** لود کردن $5 \mu\text{L}$ از محصول PCR روی ژل آگارز ۱٪ در بافر 1X TAE همراه با DNA Ladder $100\text{ bp}$.
   * تشکیل یک باند تک، شفاف و بدون پرایمر-دایمر الزامی است.
2. **خالص‌سازی محصول PCR (PCR Clean-up):**
   * جهت حذف dNTPها و پرایمرهای اضافی قبل از تعیین توالی.
   * **روش آنزیمی (ExoI/SAP):** افزودن $۰.۵ \mu\text{L}$ آنزیم Exonuclease I و $۰.۵ \mu\text{L}$ Shrimp Alkaline Phosphatase به $5 \mu\text{L}$ محصول PCR $\rightarrow$ انکوباسیون در $37^\circ\text{C}$ به مدت ۱۵ دقیقه و غیرفعال‌سازی آنزیم در $80^\circ\text{C}$ به مدت ۱۵ دقیقه.

</details>

<details>
<summary><b>مرحله ۴: واکنش تعیین توالی به روش سنگر (Sanger Sequencing)</b></summary>

1. آماده‌سازی نمونه‌ها برای تعیین توالی دوطرفه (Forward و Reverse مجزا):
   * $5 \mu\text{L}$ محصول PCR خالص‌شده.
   * $2 \mu\text{L}$ پرایمر ($3.2 \text{ pmol/\mu L}$).
   * رساندن حجم به $10-15 \mu\text{L}$ با آب دیونیزه.
2. ارسال به دستگاه تعیین توالی موئینگی (Capillary Electrophoresis).

</details>

<details>
<summary><b>مرحله ۵: آنالیز کروماتوگرام، ویرایش توالی و استعلام در PubMLST</b></summary>

1. **ارزیابی کیفیت کروماتوگرام:** باز کردن فایلهای `.ab1` یا `.scf` در نرم‌افزارهای ویرایش توالی (مانند Chromas Lite، Geneious یا BioEdit).
   * پیک‌ها باید تیز، تک‌رنگ و بدون نویز متداخل باشند (تضمین کیفیت $Phred Score > 30$).
2. **تهیه توالی اجماعی (Consensus Sequence):** هم‌ردیف‌سازی (Alignment) توالی رفت و برگشت و تصحیح خوانش‌های اشتباه در دو انتها.
3. **برش توالی (Trimming):** قیچی کردن ابتدا و انتهای توالی طبق اندازه استاندارد تعریف‌شده در PubMLST برای آن ژن خاص (مثلا دقیقاً $450\text{ bp}$).
4. **استعلام در دیتابیس PubMLST:**
   * ورود به بخش Single locus query دیتابیس باکتری مربوطه.
   * Paste کردن توالی برده‌شده و دریافت شماره آلل (Allele Number).
   * وارد کردن شماره آلل‌های ۷ ژن در بخش Allelic Profile Query جهت دریافت **Sequence Type (ST)** نهایی.

</details>

