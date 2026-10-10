# جداول استاندارد، توالی پرایمرها و راهنمای عیب‌یابی (Troubleshooting)

<details>
<summary><b>جدول ۱: توالی پرایمرهای استاندارد مورد استفاده در RAPD، ERIC و REP</b></summary>

| تکنیک | نام پرایمر | توالی نوکلئوتیدی ($5' \rightarrow 3'$) | $T_m$ پیشنهادی | کاربرد اصلی |
| :--- | :--- | :--- | :--- | :--- |
| **RAPD** | **OPA-02** | `5'-TGCCGAGCTG-3'` | $36^\circ\text{C}$ | تایپینگ عمومی باکتری‌ها و قارچ‌ها |
| **RAPD** | **OPA-09** | `5'-GGGTAACGCC-3'` | $36^\circ\text{C}$ | تایپینگ *Pseudomonas* و *Acinetobacter* |
| **ERIC-PCR** | **ERIC1R** | `5'-ATGTAAGCTCCTGGGGATTCAC-3'` | $52^\circ\text{C}$ | انتروباکتریاسه (*E. coli*, *Salmonella*) |
| **ERIC-PCR** | **ERIC2** | `5'-AAGTAAGTGACTGGGGTGAGCG-3'` | $52^\circ\text{C}$ | ترکیب با ERIC1R |
| **REP-PCR** | **REP1R-I** | `5'-IIIICGICGICATCIGGC-3'` | $40-45^\circ\text{C}$ | ژنوتایپینگ گرم منفی‌ها |
| **REP-PCR** | **REP2-I** | `5'-ICGICTTATCIGGCCTAC-3'` | $40-45^\circ\text{C}$ | ترکیب با REP1R-I |

</details>

<details>
<summary><b>جدول ۲: اجزای بافرها و آداپتورهای استاندارد تکنیک AFLP</b></summary>

| نام عنصر | توالی / ترکیب شیمیایی | نقش عملیاتی در AFLP |
| :--- | :--- | :--- |
| **EcoRI Adaptor Top** | `5'-CTGTAGACTGCGTACC-3'` | اتصال به انتهای چسبنده EcoRI روی DNA |
| **EcoRI Adaptor Bottom** | `5'-AATTGGTACGCAGTAC-3'` | تکمیل ساختار دبل‌استرند آداپتور |
| **MseI Adaptor Top** | `5'-GACGATGAGTCCTGAG-3'` | اتصال به انتهای چسبنده MseI روی DNA |
| **MseI Adaptor Bottom** | `5'-TACTCAGCACTCAT-3'` | تکمیل ساختار دبل‌استرند آداپتور |

</details>

<details>
<summary><b>جدول ۳: جدول جامع عیب‌یابی (Troubleshooting Matrix)</b></summary>

| مشکل ظاهری | علت احتمالی | اقدام اصلاحی سریع |
| :--- | :--- | :--- |
| **عدم تکرارپذیری باندها در RAPD** | ۱. نوسان در غلظت DNA ورودی.<br>۲. کیفیت متفاوت Taq Polymerase.<br>۳. نوسان دمایی ترموسایکلر. | ۱. غلظت DNA دقیقاً روی $10 \text{ ng}$ تنظیم شود.<br>۲. استفاده از Master Mix یکنواخت برای کل نمونه‌ها.<br>۳. عدم استفاده از چاهک‌های حاشیه‌ای ترموسایکلر. |
| **وجود اسمیر (Smear) شدید در ERIC/REP** | ۱. مقدار بسیار بالای DNA الگو.<br>۲. دمای اتصال (Annealing) بسیار پایین. | ۱. کاهش DNA الگو به $20-30 \text{ ng}$.<br>۲. افزایش دمای اتصال به میزان ۲ درجه. |
| **باندهای کم‌رنگ یا عدم وجود باند در AFLP** | ۱. هضم ناکامل آنزیمی.<br>۲. مهار آنزیم Ligase توسط نمک‌های اضافی. | ۱. افزایش زمان هضم آنزیمی به ۳ ساعت.<br>۲. خالص‌سازی مجدد DNA قبل از هضم. |

</details>