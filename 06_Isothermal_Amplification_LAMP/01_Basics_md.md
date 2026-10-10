# دستورالعمل اجرایی آزمایشگاهی تکثیر هم‌دما به روش LAMP (LAMP Laboratory Protocol)

## ۱. مقدمه و اصول آزمایش (Introduction & Principle)
تکنیک LAMP امکان تکثیر مستقیم DNA را در دمای ثابت ۶۵ درجه سانتی‌گراد فراهم می‌سازد. در این پروتکل از آنزیم *Bst* 2.0 DNA Polymerase و ۶ پرایمر مختلف استفاده می‌شود تا ساختارهای حلقوی (Stem-Loop) برای تکثیر بازگشتی ایجاد گردند.

---

## ۲. مراحل پیش‌نیاز و آماده‌سازی پرایمرها

### ۱-۲. بازسازی پرایمرهای LAMP (Primer Reconstitution)
پرایمرهای LAMP شامل دو پرایمر داخلی (FIP/BIP)، دو پرایمر خارجی (F3/B3) و دو پرایمر حلقه (LoopF/LoopB) هستند.

1. لوله‌های لیوفیلیزه را ۳۰ ثانیه اسپین کوتاه کنید.
2. با افزودن بافر TE، استوک ۱۰۰ میکرمولار (100 μM) تهیه کرده و ۳۰ ثانیه ورتکس کنید.
3. یک **مخلوط پرایمر کاری ۱۰X (10X Primer Mix)** به حجم کل ۵۰۰ میکرولیتر طبق جدول زیر روی یخ آماده کنید:

| نام پرایمر | غلظت استوک | غلظت در Mix (10X) | حجم مورد نیاز برای ۵۰۰μL |
| :--- | :--- | :--- | :--- |
| **FIP** | 100 μM | 16 μM | 80 μL |
| **BIP** | 100 μM | 16 μM | 80 μL |
| **F3** | 100 μM | 2 μM | 10 μL |
| **B3** | 100 μM | 2 μM | 10 μL |
| **LoopF** | 100 μM | 4 μM | 20 μL |
| **LoopB** | 100 μM | 4 μM | 20 μL |
| **Nuclease-Free Water**| - | - | 280 μL |

---

## ۳. مراحل آماده‌سازی Master Mix و واکنش (Step-by-Step Procedure)

### ۱-۳. کنترل دما و نگهداری
* تمام مواد (باقر، dNTP، MgSO4 و پرایمرها) به جز آنزیم را ذوب و ۱۰ ثانیه ورتکس و اسپین کنید.
* آنزیم *Bst* 2.0 را تا زمان مصرف در فریزر یا Cool Block نگه‌دارید و هرگز ورتکس نکنید.

### ۲-۳. جدول حجم اجزای واکنش برای یک لوله (۲۵ میکرولیتر)

| ماده / ترکیب | غلظت اولیه | غلظت نهایی در واکنش | حجم در یک واکنش (μL) |
| :--- | :--- | :--- | :--- |
| **Nuclease-Free Water** | - | - | 8.5 μL |
| **Isothermal Amplification Buffer**| 10X | 1X | 2.5 μL |
| **$\text{MgSO}_4$** | 100 mM | 8.0 mM (شامل بافر) | 1.5 μL |
| **dNTPs Mix** | 10 mM (each) | 1.4 mM each | 3.5 μL |
| **10X LAMP Primer Mix** | 10X | 1X | 2.5 μL |
| **WarmStart *Bst* 2.0 Polymerase**| 8,000 U/mL | 0.32 U/μL (8 Units) | 1.0 μL |
| **Colorimetric Indicator (WarmStart/Phenol Red)**| 50X | 1X | 0.5 μL |
| **Template DNA** | - | 1 - 10 ng | 5.0 μL |
| **حجم نهایی** | - | - | **۲۵.۰ μL** |

### ۳-۳. مخلوط‌سازی و بن‌ماری/هن‌بلوک
1. مواد فوق به جز الگو را روی یخ در یک لوله ۱.۵ میلی‌لیتری اضافه کنید.
2. با پیپتینگ آرام (۵ بار) مخلوط کرده و ۵ ثانیه‌ اسپین کوتاه کنید.
3. مقدار ۲۰ میکرولیتر از مسترمیکس را به میکروتیوب‌های 0.2ml PCR منتقل کنید.
4. مقدار ۵ میکرولیتر DNA الگو (یا آب برای کنترل منفی) اضافه کنید.
5. درب لوله‌ها را محکم ببندید و ۵ ثانیه اسپین کنید.
6. لوله‌ها را در **بن‌ماری یا هیتبلوک یا ترموسایکلر** روی دمای **۶۵ درجه سانتی‌گراد به مدت ۳۰ الی ۴۵ دقیقه** قرار دهید.
7. برای غیرفعال‌سازی آنزیم، لوله‌ها را ۵ دقیقه در دمای **۸۵ درجه سانتی‌گراد** قرار دهید.

---

## ۴. آشکارسازی و سنجش نتایج (Detection)

* **تغییر رنگ چشمی (Colorimetric):** صورت گرفتن واکنش مثبت باعث افت pH و تغییر رنگ از **صورتی به زرد** (در شناساگر Phenol Red) یا **بنفش به آبی** (در Hydroxynaphthol Blue) می‌شود.
* **نور UV/Blue Light:** در صورت افزودن SYBR Green یا Calcein، نمونه مثبت تحت نور فلورسنت درخشان می‌شود.

---

## ۵. منابع و فیلم‌های آموزشی (References & Videos)

### مراجع علمی
1. **Notomi, T., et al. (2000).** "Loop-mediated isothermal amplification of DNA." *Nucleic Acids Research*, 28(12), e63. [PubMed](https://pubmed.ncbi.nlm.nih.gov/10871382/)
2. **Nagamine, K., et al. (2002).** "Accelerating reaction by loop primers in loop-mediated isothermal amplification." *Molecular and Cellular Probes*, 16(3), 223-229.

### ویدیوهای آموزشی
* [NEB WarmStart LAMP Protocol & Colorimetric Detection Guide](https://www.youtube.com/results?search_query=NEB+LAMP+protocol)
* [Visualizing LAMP Results with SYBR Green and Phenol Red](https://www.youtube.com/results?search_query=LAMP+colorimetric+detection+protocol)