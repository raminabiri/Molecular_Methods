# پروتکل‌های جامع و عملیاتی آزمایشگاهی CRISPR-Cas

<details>
<summary><b>پروتکل ۱: طراحی In Silico و ساخت پلاسمید بیان sgRNA</b></summary>

### مرحله ۱: طراحی sgRNA برای هدف‌گیری ژن مقاومت (*bla*<sub>KPC</sub>)
1. توالی ژن *bla*<sub>KPC</sub> را از پایگاه داده GenBank دریافت کنید.
2. توالی‌های `5'-NGG-3'` (توالی PAM) را روی هر دو رشته شناسایی کنید.
3. ۲۰ نوکلئوتید مجاور سمت '5 توالی PAM را به عنوان توالی اسپیسر انتخاب کنید.
4. با استفاده از ابزارهای آنلاین (مانند Benchling یا CRISPOR)، میزان **On-target score** (بازده برش) و **Off-target score** (عدم اتصال غیر اختصاصی به ژنوم میزبان) را ارزیابی کرده و بهترین توالی را انتخاب کنید.
5. توالی اولیگونوکلئوتیدهای اورهنگ‌دار جهت کلونینگ را سفارش دهید:
   * **Top Strand:** `5'-CACCG[20-nt Spacer]-3'`
   * **Bottom Strand:** `5'-AAAC[Complement 20-nt Spacer]C-3'`

---

### مرحله ۲: آنیلینگ اولیگوها و کلونینگ در وکتور pSpCas9(BB)-2A-Puro (px459)
1. **واکنش آنیلینگ (Annealing Reaction):**
   * $1 \mu\text{L}$ اولیگوی Top ($100 \mu\text{M}$)
   * $1 \mu\text{L}$ اولیگوی Bottom ($100 \mu\text{M}$)
   * $1 \mu\text{L}$ بافر 10X T4 Ligation Buffer
   * $7 \mu\text{L}$ آب nuclease-free
   * **برنامه ترموسایکلر:** $95^\circ\text{C}$ به مدت ۵ دقیقه، سپس کاهش دما تا $25^\circ\text{C}$ با سرعت $5^\circ\text{C/min}$.

2. **هضم و لیگاسیون همزمان (One-pot Digestion-Ligation):**
   * $100 \text{ ng}$ وکتور px459
   * $2 \mu\text{L}$ از اولیگوی آنیل‌شده (رقیق‌شده ۱:۲۰۰)
   * $1 \mu\text{L}$ آنزیم هضمی BbsI (BpiI)
   * $1 \mu\text{L}$ آنزیم T4 DNA Ligase
   * $2 \mu\text{L}$ بافر T4 Ligase Buffer
   * رساندن حجم به $20 \mu\text{L}$ با آب.
   * **برنامه:** ۶ سیکل شامل ($37^\circ\text{C}$ به مدت ۵ دقیقه $\rightarrow$ $16^\circ\text{C}$ به مدت ۱۰ دقیقه)، سپس $37^\circ\text{C}$ به مدت ۳۰ دقیقه و $80^\circ\text{C}$ به مدت ۵ دقیقه.

3. **ترانسفورماسیون:** تزریق ۵ میکرولیتر از محصول به باکتری با صلاحیت *E. coli* DH5a و کشت روی محیط LB Agar حاوی آمپی‌سیلین ($100 \mu\text{g/mL}$).

</details>

<details>
<summary><b>پروتکل ۲: ویرایش ژنوم یوکاریوتی با کمپلکس RNP و الکتروپوریشن</b></summary>

استفاده از کمپلکس Ribonucleoprotein (پروتئین Recombinant Cas9 + sgRNA) مانع از Off-target بالای ناشی از بیان مداوم پلاسمید می‌شود.

### ۱. آماده‌سازی کمپلکس RNP
1. مقدار $10 \mu\text{g}$ از پروتئین Cas9 متصل به NLS را با $12 \mu\text{g}$ از sgRNA سنتزی (در نسبت مولی ۱:۱.۲) مخلوط کنید.
2. حجم را با بافر Resuspension R به $15 \mu\text{L}$ برسانید.
3. به مدت ۲۰ دقیقه در دمای اتاق ($25^\circ\text{C}$) انکوبه کنید تا کمپلکس RNP تشکیل شود.

### ۲. الکتروپوریشن سلول‌ها (مثلاً سلول‌های سرطانی A549)
1. تعداد $1 \times 10^6$ سلول را سانتریفیوژ کرده ($200 \times g$ به مدت ۵ دقیقه) و رسوب را با بافر الکتروپوریشن بشویید.
2. رسوب سلولی را در $100 \mu\text{L}$ بافر مخصوص حل کرده و به آرامی به لوله حاوی RNP اضافه کنید.
3. مخلوط را درون کووت الکتروپوریشن (Cuvette 2mm) بریزید.
4. اعمال پالس الکتریکی با دستگاه (مثلاً تنظیمات Neon Transfection: $1300 \text{ V}$، پهنای پالس $10 \text{ ms}$، ۳ پالس).
5. بلافاصله سلول‌ها را به پلیت کشت حاوی محیط گرم RPMI + 10% FBS منتقل کرده و در $37^\circ\text{C}$ با 5% CO2 انکوبه کنید.

</details>

<details>
<summary><b>پروتکل ۳: سنجش بازده ویرایش با آزمون T7 Endonuclease I (T7E1 Assay)</b></summary>

1. **استخراج DNA ژنومی:** پس از ۴۸ ساعت از ترانسفکشن، DNA ژنومی سلول‌های ویرایش‌شده و کنترل را استخراج کنید.
2. **واکنش تکثیر PCR:**
   * تکثیر ناحیه ۵۰۰ جفت‌بازی اطراف نقطه ویرایش با پرایمرهای اختصاصی.
   * بررسی خلوص محصول PCR روی ژل ۱٪.
3. **دناتوراسیون و آنیلینگ مجدد (Heteroduplex Formation):**
   * $200 \text{ ng}$ از محصول PCR را در بافر 1X NEBuffer 2 بریزید (حجم نهایی $19 \mu\text{L}$).
   * **برنامه:** $95^\circ\text{C}$ به مدت ۱۰ دقیقه $\rightarrow$ کاهش دما از $95^\circ\text{C}$ به $85^\circ\text{C}$ (با سرعت $-2^\circ\text{C/sec}$) $\rightarrow$ کاهش از $85^\circ\text{C}$ به $25^\circ\text{C}$ (با سرعت $-0.1^\circ\text{C/sec}$).
4. **هضم با T7E1:**
   * افزودن $1 \mu\text{L}$ آنزیم T7 Endonuclease I.
   * انکوباسیون در $37^\circ\text{C}$ به مدت ۱۵ دقیقه.
5. **الکتروفورز و محاسبات:**
   * الکتروفورز روی ژل آگارز ۲٪.
   * محاسبه درصد ویرایش (InDel %):
     $$\text{InDel \%} = 100 \times \left(1 - \sqrt{1 - \frac{f_a + f_b}{f_a + f_b + f_p}}\right)$$
     (که در آن $f_a$ و $f_b$ شدت باندهای برش‌خورده و $f_p$ شدت باند اولیه برش‌نخورده است).

</details>

<details>
<summary><b>پروتکل ۴: سنجش تشخیصی سریع SHERLOCK (مبتنی بر Cas13a)</b></summary>

### مرحله ۱: تکثیر ایزوترمال RPA (Recombinase Polymerase Amplification)
1. **ترکیب واکنش ($50 \mu\text{L}$):**
   * $29.5 \mu\text{L}$ بافر RPA Rehydration buffer
   * $2.4 \mu\text{L}$ پرایمر رفت ($10 \mu\text{M}$) دارای پروموتر T7
   * $2.4 \mu\text{L}$ پرایمر برگشت ($10 \mu\text{M}$)
   * $5 \mu\text{L}$ نمونه RNA/DNA استخراج‌شده
   * $2.5 \mu\text{L}$ منیزیوم استات ($280 \text{ mM}$)
2. انکوباسیون در دمای $39^\circ\text{C}$ به مدت ۲۵ دقیقه.

---

### مرحله ۲: واکنش ترانسکرپش درجا و Cleavage با LwaCas13a
1. **مخلوط واکنش تشخیصی ($20 \mu\text{L}$):**
   * $45 \text{ nM}$ پروتئین LwaCas13a
   * $22.5 \text{ nM}$ crRNA اختصاصی ژن مقاومت (*bla*<sub>NDM-1</sub>)
   * $125 \text{ nM}$ پروب گزارشگر ssRNA (مثلاً `5'-FAM-UUUUUU-BHQ1-3'`)
   * $0.5 \mu\text{L}$ آنزیم T7 RNA Polymerase
   * $1 \text{ mM}$ از rNTPs
   * $2 \mu\text{L}$ از محصول RPA مرحله قبل.
2. **آشکارسازی:**
   * انکوباسیون در $37^\circ\text{C}$ به مدت ۳۰ دقیقه در دستگاه فلورومتر (ثبت سیگنال FAM).
   * **یا** استفاده از نوار لاترال فلو (Lateral Flow Strip): افزودن بافر شستشو و وارد کردن نوار بیدهای طلایی، مشاهده خط تست ظرف ۵ دقیقه.

</details>

<details>
<summary><b>پروتکل ۵: منابع و فیلم‌های آموزشی آزمایشگاهی</b></summary>

1. **JoVE (Journal of Visualized Experiments):** *Genome Editing in Human Cells Using CRISPR-Cas9 Ribonucleoprotein Complexes* (پروتکل ویدئویی کامل RNP).
2. **Addgene Video Protocol Series:** *CRISPR Gel Electrophoresis & T7E1 Assay Walkthrough* (مراحل عملی T7E1).
3. **Broad Institute Diagnostics Initiative:** *Step-by-step SHERLOCK & DETECTR Protocol Guide* (ویدئوی آموزشی کار با نوار لاترال فلو و Cas13).

</details>