# جداول استاندارد ژن‌ها، پرایمرها و راهنمای جامع عیب‌یابی MLST

<details>
<summary><b>جدول ۱: طرح استاندارد MLST برای پاتوژن‌های شایع باکتریایی</b></summary>

| نام باکتری | تعداد ژن‌ها | لیست ژن‌های خانه‌دار | اندازه قطعه نهایی (bp) | دمای Annealing | دیتابیس مرجع |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ***Klebsiella pneumoniae*** | ۷ ژن | *gapA, infB, mdh, pgi, phoE, rpoB, tonB* | $450 - 500 \text{ bp}$ | $50^\circ\text{C} - 58^\circ\text{C}$ | Pasteur / PubMLST |
| ***Escherichia coli*** | ۷ ژن | *adk, fumC, gyrB, icd, mdh, purA, recA* | $400 - 530 \text{ bp}$ | $54^\circ\text{C} - 58^\circ\text{C}$ | EnteroBase / Achtman |
| ***Staphylococcus aureus*** | ۷ ژن | *arcC, aroE, glpF, gmk, pta, tpi, yqiL* | $400 - 510 \text{ bp}$ | $55^\circ\text{C}$ | PubMLST |
| ***Pseudomonas aeruginosa*** | ۷ ژن | *acsA, aroE, guaA, mutL, nuoD, ppsA, trpE* | $390 - 520 \text{ bp}$ | $58^\circ\text{C} - 60^\circ\text{C}$ | PubMLST |
| ***Acinetobacter baumannii*** | ۷ ژن | *gltA, gyrB, gdhB, recA, cpn60, gpi, rpoD* | $350 - 500 \text{ bp}$ | $55^\circ\text{C}$ | PubMLST (Pasteur scheme) |

</details>

<details>
<summary><b>جدول ۲: نمونه پروفایل آللی و تعیین ST برای چند باکتری شاخص</b></summary>

| گونه باکتری | *Gene 1* | *Gene 2* | *Gene 3* | *Gene 4* | *Gene 5* | *Gene 6* | *Gene 7* | **Sequence Type (ST)** | اهمیت کلینیکی / اپیدمولوژیک |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ***K. pneumoniae*** | $gapA: 2$ | $infB: 1$ | $mdh: 1$ | $pgi: 1$ | $phoE: 1$ | $rpoB: 1$ | $tonB: 79$ | **ST258** | کلون فوق‌العاده مقاوم به کارباپنم (KPC) |
| ***E. coli*** | $adk: 6$ | $fumC: 4$ | $gyrB: 14$ | $icd: 16$ | $mdh: 24$ | $purA: 8$ | $recA: 14$ | **ST131** | کلون جهانی تولیدکننده ESBL (CTX-M-15) |
| ***S. aureus*** | $arcC: 2$ | $aroE: 2$ | $glpF: 2$ | $gmk: 2$ | $pta: 6$ | $tpi: 3$ | $yqiL: 2$ | **ST5 (CC5)** | کلون اصلی MRSA بیمارستانی (HA-MRSA) |

</details>

<details>
<summary><b>جدول ۳: ماتریس کامل عیب‌یابی خطاهای MLST (Troubleshooting)</b></summary>

| اشکال مشاهده شده | علت احتمالی | اقدام اصلاحی و راهکار |
| :--- | :--- | :--- |
| **عدم تکثیر باند PCR (No Band)** | ۱. دمای Annealing بسیار بالا.<br>۲. کیفیت پایین DNA الگوی اولیه.<br>۳. وجود ناهماهنگی پرایمر با زیرگونه خاص. | ۱. کاهش دما به میزان $2-4^\circ\text{C}$ (استفاده از Gradient PCR).<br>۲. استخراج مجدد DNA با کیت ستونی.<br>۳. چک کردن توالی پرایمر در دیتابیس. |
| **وجود باندهای نام اختصاصی/اسمیر** | ۱. دمای اتصال پرایمر بسیار پایین.<br>۲. غلظت بالای MgCl2 یا پرایمر.<br>۳. تعداد سیکل‌های زیاد PCR. | ۱. افزایش دمای Annealing.<br>۲. کاهش غلظت پرایمر به $0.2 \mu\text{M}$.<br>۳. کاهش سیکل‌ها به ۳۰ سیکل. |
| **پیک‌های دوگانه (Double Peaks) در کروماتوگرام** | ۱. آلودگی نمونه با باکتری دیگر.<br>۲. تکثیر همزمان دو پارالوگ ژنی.<br>۳. وجود پرایمرهای اضافی در واکنش. | ۱. کشت مجدد و اطمینان از کلونی تک.<br>۲. بهینه‌سازی اختصاصیت PCR.<br>۳. خالص‌سازی مجدد محصول PCR قبل از سنگر. |
| **عدم شناسایی آلل در PubMLST** | ۱. برش (Trimming) نادرست توالی.<br>۲. وجود خطای خوانش در انتهای توالی.<br>۳. کشف یک **آلل جدید (New Allele)**. | ۱. چک کردن اندازه دقیق قطعه با توالی‌های مرجع.<br>۲. بررسی مجدد کروماتوگرام رفت و برگشت.<br>۳. سابمیت توالی جدید به پشتیبان PubMLST جهت دریافت کد جدید. |

</details>

