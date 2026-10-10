# جداول استاندارد، ماتریس مقایسه‌ای و راهنمای عیب‌یابی CRISPR-Cas

<details>
<summary><b>جدول ۱: مقایسه کامل خصوصیات افکتورهای مختلف CRISPR-Cas</b></summary>

| ویژگی / پارامتر | SpCas9 | SaCas9 | Cas12a (Cpf1) | Cas13a (C2c2) |
| :--- | :--- | :--- | :--- | :--- |
| **کلاس / تیپ** | Class 2 / Type II | Class 2 / Type II | Class 2 / Type V | Class 2 / Type VI |
| **مولکول هدف اصلی** | dsDNA | dsDNA | dsDNA | **ssRNA** |
| **توالی PAM / PFS** | `5'-NGG-3'` | `5'-NNGRRT-3'` | `5'-TTTV-3'` | PFS در سمت '3 (A, C, U) |
| **نوع انتهای برش** | انتهای صاف (Blunt) | انتهای صاف (Blunt) | انتهای چسبنده (Staggered) | برش غیر اختصاصی RNA |
| **نیاز به tracrRNA** | **بله** | **بله** | **خیر** | **خیر** |
| **فعالیت Trans-cleavage**| ندارد | ندارد | **دارد (روی ssDNA)** | **دارد (روی ssRNA)** |
| **اندازه پروتئین** | ۱۳۶۸ اسید آمینه ($158 \text{ kDa}$) | ۱۰۵۳ اسید آمینه ($124 \text{ kDa}$) | حدود ۱۲۰۰ اسید آمینه | حدود ۱۱۵۰ اسید آمینه |
| **کاربرد اصلی** | ویرایش ژنوم کلی | بسته بندی در AAV | ویرایش ژنوم + DETECTR | تشخیص SHERLOCK + ویرایش RNA |

</details>

<details>
<summary><b>جدول ۲: ماتریس پلتفرم‌های تشخیصی مبتنی بر CRISPR</b></summary>

| پلتفرم تشخیصی | آنزیم اصلی | هدف شناسایی | روش پیش‌تکثیر | نوع گزارشگر (Reporter) | حد تشخیص (LOD) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SHERLOCK v2** | LwaCas13a / AsCas12a | RNA یا DNA | RPA + T7 Transcription | ssRNA / ssDNA Reporter | **Attomolar ($10^{-18} \text{ M}$)** |
| **DETECTR** | LbCas12a | dsDNA | LAMP یا RPA | ssDNA Fluorophore-Quencher | Attomolar |
| **STOPCovid** | AapCas12b | viral RNA | LAMP در یک لوله (Single-step) | ssDNA Fluorescence/LFA | 10 copies/$\mu\text{L}$ |
| **FELUDA** | FnCas9 (Dead) | DNA (SNVs) | RT-PCR | Biotin-labeled DNA | Femtomolar |

</details>

<details>
<summary><b>جدول ۳: جدول عیب‌یابی جامع (Troubleshooting Matrix)</b></summary>

| مشکل ظاهری | علت احتمالی | اقدام اصلاحی سریع |
| :--- | :--- | :--- |
| **عدم مشاهده هیچ‌گونه ویرایشی در T7E1** | ۱. On-target score پایین gRNA.<br>۲. بازده ترانسفکشن کم.<br>۳. انکوباسیون ناکافی RNP. | ۱. بازطراحی sgRNA در سایت جدید.<br>۲. بهینه‌سازی ولتاژ الکتروپوریشن یا کیفیت پلاسمید.<br>۳. افزودن NLS به Cas9. |
| **میزان Off-target بسیار بالا** | ۱. بیان طولانی‌مدت Cas9 از پلاسمید.<br>۲. غلظت بالای RNP. | ۱. سوئیچ به سیستم RNP به جای پلاسمید.<br>۲. استفاده از High-Fidelity Cas9 (SpCas9-HF1). |
| **سیگنال پس‌زمینه (Background) بالا در SHERLOCK** | ۱. آلودگی RNase در بافرها.<br>۲. تخریب پروب RNA به‌صورت خودبه‌خودی. | ۱. استفاده از آب DEPC-treated و مهارکننده RNase.<br>۲. کاهش زمان انکوباسیون ترانسکرپشن. |
| **مرگ شدید سلول‌ها پس از الکتروپوریشن** | ۱. ولتاژ یا شوک الکتریکی بسیار بالا.<br>۲. تراکم نادرست سلولی. | ۱. کاهش ولتاژ پالس به میزان ۱۰۰ ولت.<br>۲. استفاده از محیط کشت فاقد آنتی‌بیوتیک پس از شوک. |

</details>