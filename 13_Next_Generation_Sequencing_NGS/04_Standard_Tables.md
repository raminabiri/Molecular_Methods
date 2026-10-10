# جداول استاندارد، ماتریس مقایسه پلتفرم‌ها و راهنمای عیب‌یابی (Troubleshooting)

<details>
<summary><b>جدول ۱: مقایسه جامع پلتفرم‌های تعیین توالی</b></summary>

| مشخصه / پارامتر | Illumina (NovaSeq) | PacBio (Sequel IIe) | Oxford Nanopore (PromethION) | Ion Torrent (GeneStudio) |
| :--- | :--- | :--- | :--- | :--- |
| **نوع خوانش** | Short-Read | Long-Read (HiFi) | Ultra-Long Read | Short-Read |
| **مکانیسم** | Synthesis (SBS) | Real-Time SMRT | Ionic Current Blockade | Semiconductor pH |
| **طول خوانش** | $2 \times 150 \text{ bp}$ | $10-25 \text{ kb}$ | $10 \text{ kb} - > 1 \text{ Mb}$ | $200-400 \text{ bp}$ |
| **دقت (Accuracy)** | $> 99.9\%$ (Q30) | $> 99.9\%$ (Q30) | $99.0 - 99.5\%$ | $99.0\%$ |
| **خطای اصلی** | Substitution | Indel جزئی | Indel در Homopolymers | Indel در Homopolymers |
| **آنالیز اپی‌ژنوم** | نیاز به Bisulfite | مستقیم (از روی IPD) | مستقیم (از روی جریان) | نیاز به Bisulfite |

</details>

<details>
<summary><b>جدول ۲: راهنمای عیب‌یابی کیفیت لایبرری و ران NGS</b></summary>

| مشکل ظاهری | علت احتمالی | راهکار اصلاحی |
| :--- | :--- | :--- |
| **داده‌های خروجی دارای دایمر آداپتور (Adapter Dimers)** | خالص‌سازی ناکافی با بیدهای AMPure XP پس از Ligation. | تکرار شستشو با بیدهای مغناطیسی در نسبت 0.6X-0.8X. |
| **افت شدید کیفیت (Q-score) در انتهای خوانش R2 در ایلومینا** | آکوموله شدن مواد شیمیایی و آسیب آنزیمی در چرخه‌های بالا. | تنظیم تعداد سیکل‌ها یا سوئیچ به کیت‌های با خلوص بالاتر. |
| **تراکم بالای خوشه‌ها (Overclustering) روی Flow Cell** | غلظت بالای لایبرری بارگذاری‌شده روی فلوسل. | رقیق‌سازی دقیق لایبرری با روش Fluorometric (Qubit/qPCR). |

</details>