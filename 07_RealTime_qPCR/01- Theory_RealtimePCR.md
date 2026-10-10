# مبانی جامع، مهندسی سیستم‌ها و سیستم‌های سنجش در Real-Time PCR (qPCR)

---

## ۱. تئوری و اصول پایه Real-Time PCR
در تکنیک Real-Time PCR (یا Quantitative PCR)، تکثیر قطعات DNA در هر سیکل به صورت لحظه‌ای با استفاده از سیگنال‌های فلورسنت پایش می‌شود. بر خلاف PCR معمولی که آنالیز آن در مرحله انتهای واکنش (End-Point) انجام می‌گیرد، qPCR ارزیابی را در فاز نمایی (Exponential Phase) انجام می‌دهد.

### مفاهیم کلیدی و منحنی تکثیر (Amplification Curve):
* **فاز نمایی (Exponential Phase):** مرحله‌ای که واکنش با راندمان ۱۰۰٪ رخ می‌دهد ($2^N$) و دقیق‌ترین زمان برای اندازه‌گیری مقدار اولیه DNA الگو است.
* **خط آستانه (Threshold Line):** خطی مستطیلی و افقی بالاتر از سیگنال‌های نویز زمینه (Background Noise).
* **چرخه آستانه ($C_t$ یا $C_q$):** شماره سیکلی که در آن شدت فلورسانس نمونه از خط آستانه عبور می‌کند. هر چه $C_t$ کمتر باشد، میزان اولیه DNA target بیشتر بوده است.

---

## ۲. سیستم‌های گزارش‌دهی فلورسانس (Chemistry Systems)

### ۲.۱. رنگ‌های متصل‌شونده به DNA غیر اختصاصی (SYBR Green I)
* **مکانیسم:** این رنگ به شیار کوچک (Minor Groove) دنای دو رشته‌ای (dsDNA) متصل شده و سیگنال نشر می‌دهد.
* **مزایا:** ارزان، ساده، بدون نیاز به طراحی پرایمر اختصاصی.
* **معایب:** اتصال غیر اختصاصی به دیمر پرایمر یا محصولات فرعی. نیاز الزامی به **آنالیز منحنی ذوب (Melt Curve Analysis)** دارد.

### ۲.۲. پروب‌های اختصاصی (TaqMan Probes / Hydrolysis Probes)
* **مکانیسم:** پروب حاوی یک گزارشگر (Reporter Fluorophore) در انتهای '5 و یک خاموش‌کننده (Quencher) در انتهای '3 است. اثر **FRET** در حالت عادی مانع نشر فلورسانس می‌شود. با فعالیت '5$\rightarrow$'3 اگزرونوکلئازی آنزیم Taq Polymerase در حین بسط، پروب هیدرولیز شده و Reporter آزاد می‌گردد.
* **مزایا:** اختصاصیت فوق‌العاده بالا، امکان Multiplexing با رنگ‌های مختلف.

---

## ۳. مهندسی دستگاه‌های Real-Time PCR

یک دستگاه Real-Time PCR از سه بخش مهندسی اصلی تشکیل شده است:
1. **بلوک ترمال (Thermal Block/Cycler):** تنظیم دقیق دما بر پایه فناوری المان‌های پلتیر (Peltier Elements) یا سیستم‌های جریان هوای گرم (Rotary Air-based).
2. **منبع برانگیختگی (Excitation Source):**
   * **LEDs:** طول عمر بالا، پایداری منبع نور، دامنه طیفی مشخص.
   * **لامپ‌های هالوژن/تنگستن:** طیف وسیع اما طول عمر محدود و تولید حرارت.
   * **لیزرها:** قدرت برانگیختگی بسیار بالا.
3. **آشکارساز (Detection System):**
   * **CCD / sCMOS Camera:** تصویربرداری هم‌زمان از کل پلیت.
   * **Photomultiplier Tubes (PMT):** حساست فوق‌العاده بالا همراه با فیبر نوری برای ردیابی کانال به کانال.

---

## ۴. معیارهای انتخاب فلوروفورها برای Multiplex qPCR

برای طراحی یک واکنش Multi-target بدون هم‌پوشانی طیفی (Spectral Overlap/Crosstalk)، باید فلوروفورها بر اساس مشخصات دستگاه انتخاب شوند:

| نام فلوروفور (Reporter) | طول موج تحریک (nm) | طول موج نشر (nm) | Quencher مناسب | کانال رایج دستگاه |
| :--- | :--- | :--- | :--- | :--- |
| **FAM / SYBR Green** | 495 | 520 | BHQ-1 / TAMRA | Channel 1 (FAM) |
| **HEX / VIC / JOE** | 535 | 555 | BHQ-1 | Channel 2 (HEX/VIC) |
| **ROX / Texas Red** | 585 | 605 | BHQ-2 | Channel 3 (ROX) |
| **Cy5** | 650 | 670 | BHQ-3 | Channel 4 (Cy5) |

---

## ۵. مقایسه پلتفرم‌ها و برندهای معتبر جهان

| مشخصه فنی | Applied Biosystems (QuantStudio 5/7) | Bio-Rad (CFX96 Touch) | Qiagen (Rotor-Gene Q) |
| :--- | :--- | :--- | :--- |
| **سیستم ترمال** | Peltier Block (VeriFlex) | Peltier Block | Rotary Air System |
| **منبع نور** | BrightWhite LED | 6 LEDs | LEDs با فیبر نوری |
| **آشکارساز** | CMOS | 6 Photodiodes | PMT |
| **یکواختی دمایی** | $\pm 0.25^\circ\text{C}$ | $\pm 0.4^\circ\text{C}$ | $\pm 0.01^\circ\text{C}$ (بسیار بالا) |
| **مزیت اصلی** | نرم‌افزار قدرتمند و پایداری بالا | کاربری آسان و انعطاف‌پذیری پلیت | یکواختی بی‌نظیر دما و سرعت بالا |

---

## ۶. منابع علمی و ویدیوهای آموزشی
1. **Bustin, S. A., et al. (2009).** *The MIQE guidelines: minimum information for publication of quantitative real-time PCR experiments.* Clinical Chemistry.
2. [فیلم آموزشی مهندسی اپتیک دستگاه‌های qPCR (یوتیوب)](https://www.youtube.com/results?search_query=qPCR+optical+system+engineering)
3. [آموزش مکانیسم پروب‌های TaqMan در مقابل SYBR Green](https://www.youtube.com/results?search_query=TaqMan+vs+SYBR+Green+mechanism)