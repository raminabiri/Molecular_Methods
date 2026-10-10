# تئوری جامع و تخصصی تکنیک‌های RAPD ،ERIC-PCR ،REP-PCR و AFLP

<details>
<summary><b>فصل ۱: تئوری و مبانی تکنیک RAPD (Random Amplification of Polymorphic DNA)</b></summary>

### ۱.۱. مکانیسم و اصول مولکولی
تکنیک RAPD یک روش تایپینگ مبتنی بر PCR است که **بدون نیاز به آگاهی قبلی از توالی ژنوم** (Genome sequence-independent) انجام می‌شود.
* **پرایمرها:** استفاده از یک پرایمر تک‌رشته‌ای بسیار کوتاه (معمولاً ۱۰ نوکلئوتیدی با محتوای GC بالای ۶۰٪).
* **اتصال غیر اختصاصی:** پرایمر در دمای اتصال (Annealing Temperature) بسیار پایین ($35-37^\circ\text{C}$) به چندین جایگاه مکمل یا نیمه‌مکمل روی هر دو رشته DNA وصل می‌شود.
* **شرایط تکثیر:** اگر دو جایگاه اتصال پرایمر در جهت عکس یکدیگر و در فاصله‌ای مناسب (معمولاً بین ۲۰۰ تا ۳۰۰۰ جفت‌باز) قرار داشته باشند، قطعه بین آن‌ها تکثیر شده و الگوی باند ایجاد می‌کند.

### ۱.۲. مزایا و محدودیت‌های اصلی
* **مزایا:** سریع، ارزان، عدم نیاز به اطلاعات sequence، احتیاج به مقدار بسیار کم DNA.
* **چالش بزرگ (Reproducibility):** **تکرارپذیری بسیار پایین!** این روش به شدت به تغییرات جزئی در کیفیت DNA، غلظت آنزیم، برند ترموسایکلر و غلظت $MgCl_2$ حساس است.

</details>

<details>
<summary><b>فصل ۲: تئوری و مبانی تکنیک‌های REP-PCR و ERIC-PCR (Repetitive Element PCR)</b></summary>

این دو روش بر پایه تکثیر توالی‌های تکراری غیرکدکننده محافظت‌شده در ژنوم باکتری‌ها (بویژه گرم منفی‌ها) استوار هستند.

### ۲.۱. تکنیک REP-PCR (Repetitive Extragenic Palindromic)
* **توالی هدف:** عناصر REP توالی‌های ۳۸ جفت‌بازی دارای ساختار Stem-loop هستند که به صورت چندتایی در مناطق غیرکدکننده ژنوم باکتری قرار دارند.
* **پرایمرها:** استفاده از پرایمرهای اختصاصی مانند REP1R-I و REP2-I.
* **مکانیسم:** پرایمرها به عناصر تکراری متصل شده و فاصله بین دو عنصر REP مجاور در ژنوم را تکثیر می‌کنند.

### ۲.۲. تکنیک ERIC-PCR (Enterobacterial Repetitive Intergenic Consensus)
* **توالی هدف:** عناصر ERIC توالی‌های ۱۲۶ جفت‌بازی محافظت‌شده در مناطق بین ژنی باکتری‌های انتروباکتریاسه (مثل *E. coli*, *Salmonella*, *Klebsiella*) هستند.
* **پرایمرها:** استفاده از جفت پرایمر ERIC1R و ERIC2.
* **ویژگی‌ها:** تکرارپذیری بسیار بالاتر نسبت به RAPD و توان تفکیک عالی برای اپیدمولوژی طغیان‌های بیمارستانی.

</details>

<details>
<summary><b>فصل ۳: تئوری و اصول پیشرفته تکنیک AFLP (Amplified Fragment Length Polymorphic)</b></summary>

تکنیک AFLP ترکیبی بسیار قدرتمند از هضم آنزیمی (Restriction Digestion) و PCR اختصاصی است که استاندارد طلایی fingerprinting محسوب می‌شود.

### ۳.۱. مراحل چهارگانه AFLP
1. **هضم آنزیمی دوگانه (Restriction Digestion):** هضم DNA ژنومی با یک آنزیم کم‌برش (Rare-cutter مثل *MseI* یا *EcoRI*) و یک آنزیم پربرش (Frequent-cutter مثل *TaqI*).
2. **اتصال آداپتورها (Ligation):** اتصال قطعات کوتاه دبل‌استرند (Adaptors) به انتهای قطعات هضم‌شده.
3. **پیش‌تکثیر (Pre-selective PCR):** تکثیر قطعات با پرایمرهای مکمل آداپتور که دارای یک نوکلئوتید انتخاب‌کننده در سمت '3 هستند (مثلاً $+A$).
4. **تکثیر انتخابی (Selective PCR):** تکثیر با پرایمرهایی که دارای ۲ تا ۳ نوکلئوتید انتخابی اضافه در سمت '3 هستند (مثلاً $+AAC$). این کار تعداد باندهای تکثیرشده را به ۵۰ تا ۱۰۰ باند قابل سنجش کاهش می‌دهد.

### ۳.۲. مزایا و کارآمدی
* **تکرارپذیری فوق‌العاده بالا:** برخلاف RAPD کاملاً تکرارپذیر است.
* **Power of Discrimination بالا:** قادر به تفکیک سویه‌ها حتی در سطح زیرگونه است.

</details>

<details>
<summary><b>فصل ۴: مقایسه جامع و ماتریس تصمیم‌گیری بین ۴ روش</b></summary>

| ویژگی / مشخصه | RAPD | ERIC-PCR | REP-PCR | AFLP |
| :--- | :--- | :--- | :--- | :--- |
| **مبنای مولکولی** | اتصال تصادفی پرایمر ۱۰-مر | اتصال به توالی‌های ERIC | اتصال به توالی‌های REP | هضم آنزیمی + PCR انتخابی |
| **تکرارپذیری (Reproducibility)** | بسیار پایین | متوسط تا بالا | متوسط تا بالا | **فوق‌العاده بالا** |
| **پیچیدگی پروتکل** | بسیار ساده | ساده | ساده | پیچیده و چند مرحله‌ای |
| **هزینه** | بسیار ارزان | ارزان | ارزان | نسبتاً گران |
| **نیاز به اطلاعات ژنومی** | ندارد | فقط وجود عناصر ERIC | فقط وجود عناصر REP | ندارد |
| **آنالیز خروجی** | ژل آگارز | ژل آگارز / الکتروفورز مویین | ژل آگارز / الکتروفورز مویین | Capillary Sequencer / PAGE |

</details>

<details>
<summary><b>فصل ۵: مقالات مرجع و فیلم‌های آموزشی پیشنهادی</b></summary>

### مقالات مرجع (Reference Publications)
1. **Williams, J. G., et al. (1990).** *DNA polymorphisms amplified by arbitrary primers are useful as genetic markers.* **Nucleic Acids Research**, 18(22), 6531-6535. (مقاله اصلی RAPD).
2. **Versalovic, J., et al. (1991).** *Distribution of repetitive DNA sequences in eubacteria and application to fingerprinting of bacterial genomes.* **Nucleic Acids Research**, 19(24), 6823-6831. (مقاله اصلی REP و ERIC).
3. **Vos, P., et al. (1995).** *AFLP: a new technique for DNA fingerprinting.* **Nucleic Acids Research**, 23(21), 4407-4414. (مقاله اصلی کشف AFLP).

### فیلم‌ها و ویدئوهای آموزشی
1. **JoVE (Journal of Visualized Experiments):** *Bacterial Typing using REP-PCR and ERIC-PCR Protocols*.
2. **Applied Biosystems Video Tutorial:** *Principles of AFLP Technology and Capillary Electrophoresis Analysis*.
3. **Thermo Fisher Scientific:** *Optimization of Random Amplified Polymorphic DNA (RAPD) Reactions*.

</details>