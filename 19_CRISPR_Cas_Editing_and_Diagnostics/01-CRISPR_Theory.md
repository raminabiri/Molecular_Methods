# تئوری جامع، بیولوژی مولکولی و کاربردهای پیشرفته CRISPR-Cas

<details>
<summary><b>فصل ۱: مبانی بیولوژیکی و ساختارهای مولکولی سیستم CRISPR-Cas</b></summary>

### ۱.۱. ساختار آرایه‌های CRISPR و ژن‌های Cas
سیستم CRISPR-Cas یک سیستم ایمنی تطپذیری (Adaptive Immune System) در پروکاریوت‌ها (باکتری‌ها و آرکی‌ها) است که علیه عناصر ژنتیکی بیگانه (فاژها و پلاسمیدها) عمل می‌کند.
* **CRISPR Array:** شامل توالی‌های تکراری مستقیم (Direct Repeats) است که توسط توالی‌های متغیر به نام **Spacers** از هم جدا شده‌اند. اسپیسرها در واقع قطعات غصب‌شده از DNA فاژها و پلاسمیدهای مهاجم قبلی هستند.
* **Cas Genes:** ژن‌های مجاور آرایه که آنزیم‌های نوکلئاز، هلیکاز و پروتئین‌های تطابق را کد می‌کنند.

### ۱.۲. مراحل سه گانه ایمنی باکتریایی
1. **Adaptation (Acquisition):** شناسایی DNA بیگانه توسط کمپلکس Cas1-Cas2 و بریدن و درج یک قطعه جدید (به عنوان اسپیسر) در آرایه CRISPR.
2. **Expression & Processing:** ترانسکرایب شدن آرایه CRISPR به pre-crRNA و سپس برش و پردازش آن توسط RNase III یا خود پروتئین Cas به **crRNA**های بالغ.
3. **Interference:** هدایت آنزیم نوکلئاز Cas توسط crRNA (به همراه tracrRNA در سیستم کلاس ۲) به سمت DNA/RNA بیگانه و ایجاد شکست دو رشته‌ای (DSB) یا تک‌رشته‌ای.

---

### ۱.۳. نقش حیاتی توالی PAM (Protospacer Adjacent Motif)
* **تعریف:** یک توالی کوتاه ۲ تا ۶ نوکلئوتیدی (مانند `5'-NGG-3'` برای SpCas9) که مستقیماً در سمت '3 توالی هدف روی DNA بیگانه قرار دارد.
* **مکانیسم تفکیک Self از Non-Self:** آرایه CRISPR درون کروموزوم باکتری فاقد توالی PAM است؛ بنابراین آنزیم Cas کروموزوم خودی را نمی‌برد. اما DNA فاژ حاوی PAM است و هدف قطع قرار می‌گیرد.
* **Seed Region:** ۸ تا ۱۲ نوکلئوتید مجاور PAM در sgRNA که حساسیت بالایی به عدم تطابق (Mismatch) دارد و باز شدن مارپیچ DNA را کلید می‌زند.

</details>

<details>
<summary><b>فصل ۲: دسته‌بندی و طبقه‌بندی جامع سیستم‌های CRISPR-Cas</b></summary>

سیستم‌های CRISPR بر اساس ساختار افکتور (Effector) به دو کلاس، ۶ تیپ (Type) و ده‌ها ساب‌تیپ تقسیم می‌شوند:

### ۲.۱. کلاس ۱ (Class 1) - سیستم‌های چندپروتئینی (Multi-subunit Effectors)
در این سیستم‌ها، یک کمپلکس از چند پروتئین مختلف برای برش استفاده می‌شود (شامل ۷۴٪ کل سیستم‌های پروکاریوتی).
* **Type I:** استفاده از کمپلکس **Cascade** و نوکلئاز/هلیکاز **Cas3** برای تخریب DNA.
* **Type III:** استفاده از کمپلکس **Cmr/Csm** و آنزیم **Cas10** برای تخریب همزمان DNA و RNA (دارای فعالیت تولید پیام‌رسان دوم cOA).
* **Type IV:** سیستم‌های ساده‌تر بدون فعالیت نوکلئازی روشن، معمولاً روی پلاسمیدها.

---

### ۲.۲. کلاس ۲ (Class 2) - سیستم‌های تک‌پروتئینی (Single-protein Effectors)
یک پروتئین تک‌رشته‌ای بزرگ تمام وظایف شناسایی و برش را انجام می‌دهد (ایده‌آل برای مهندسی ژنتیک).

#### ۱. Type II (Cas9):
* **ساختار دامنه‌ها:** دارای دو دامنه نوکلئازی مجزا:
  * دامنه **HNH:** رشته مکمل gRNA (Target strand) را می‌برد.
  * دامنه **RuvC:** رشته غیر مکمل (Non-target strand) را می‌برد.
* **نتیجه برش:** ایجاد شکست دو رشته‌ای با **انتهای صاف (Blunt-end)** در ۳ نوکلئوتیدی بالای PAM.

#### ۲. Type V (Cas12a / Cpf1):
* **ویژگی‌ها:** فقط به crRNA نیاز دارد (بدون نیاز به tracrRNA).
* **PAM:** توالی‌های غنی از تیمین (`5'-TTTV-3'`).
* **نتیجه برش:** ایجاد انتهای ناهموار و چسبنده (**Staggered/Sticky ends** با ۴ تا ۵ نوکلئوتید اورهنگ در سمت '5).
* **فعالیت Trans-cleavage (Collateral Cleavage):** پس از اتصال و بریدن DNA هدف cis، دامنه RuvC آن فعال شده و به‌صورت غیراختصاصی هر **ssDNA** آزاد در محیط را تخریب می‌کند (پایه تشخیص DETECTR).

#### ۳. Type VI (Cas13a, b, c):
* **هدف:** **فقط RNA** را هدف قرار می‌دهد (دارای دامنه‌های HEPN).
* **فعالیت Trans-cleavage:** پس از اتصال به RNA هدف، تمامی **ssRNA**های مجاور را به‌صورت غیراختصاصی می‌برد (پایه تشخیص SHERLOCK).

</details>

<details>
<summary><b>فصل ۳: کاربردهای پیشرفته ویرایش ژنوم و مهندسی اپی‌ژنتیک</b></summary>

### ۳.۱. مسیرهای ترمیم شکست DNA (NHEJ vs HDR)
* **NHEJ (Non-Homologous End Joining):** ترمیم سریع و دارای خطا. باعث ایجاد جهش‌های درج/حذف (InDels) و خروج ژن از چارچوب خواندن (Frame-shift) و در نتیجه **Knockout** ژن می‌شود.
* **HDR (Homology-Directed Repair):** ترمیم دقیق با استفاده از یک الگو (Donor DNA). امکان درج توالی دلخواه (**Knock-in**) یا اصلاح جهش‌های نقطه‌ای را فراهم می‌سازد.

---

### ۳.۲. تکنولوژی‌های نسل جدید (Base Editing & Prime Editing)
* **Base Editors (BE):** اتصال dCas9 یا Cas9 Nickase به آنزیم‌های دآمیناز (Cytidine یا Adenine Deaminase).
  * **CBE:** تبدیل $C \cdot G \rightarrow T \cdot A$ بدون ایجاد DSB.
  * **ABE:** تبدیل $A \cdot T \rightarrow G \cdot C$ بدون ایجاد DSB.
* **Prime Editing (PE):** اتصال Cas9 Nickase به آنزیم **Reverse Transcriptase (RT)** و استفاده از **pegRNA** (پرایم ادیتینگ gRNA). امکان انجام انواع درج، حذف و جایگزینی بدون نیاز به DSB و الگوهای Donor خارجی.

---

### ۳.۳. تنظیم بیان ژن و اپی‌ژنتیک (CRISPRa / CRISPRi)
با ایجاد **dCas9 (Dead Cas9)** که جهش در دامنه‌های HNH و RuvC دارد، قدرت برش سلب شده ولی قدرت اتصال باقی می‌ماند:
* **CRISPRi (Inhibition):** اتصال dCas9-KRAB به پروموتر جهت بلوک فیزیکی RNA Polymerase و خاموش کردن بیان ژن.
* **CRISPRa (Activation):** اتصال dCas9-VPR یا dCas9-VP64 جهت باز فراخوانی فاکتورهای ترانسکرپسیونی و افزایش شدید بیان ژن.

</details>

<details>
<summary><b>فصل ۴: کاربرد تخصصی CRISPR-Cas در مبارزه با مقاومت دارویی و آنتی‌بیوتیکی</b></summary>

مقاومت دارویی در باکتری‌ها (Antibiotic Resistance) و سلول‌های سرطانی (Chemoresistance) یکی از بزرگترین چالش‌های پزشکی مدرن است.

### ۴.۱. آنتی‌بیوتیک‌های هوشمند مبتنی بر CRISPR (CRISPR-based Antimicrobials)
برخلاف آنتی‌بیوتیک‌های کلاسیک که فلور طبیعی بدن را نابود می‌کنند، CRISPR می‌تواند به‌صورت **کُشنده اختصاصی توالی (Sequence-specific Killer)** عمل کند:

1. **تخریب ژن‌های مقاومت کروموزومی:**
   * طراحی sgRNA علیه ژن‌های مقاومت آنتی‌بیوتیکی مانند *bla*<sub>NDM-1</sub>، *bla*<sub>KPC</sub> (مقاومت به کارباپنم در *Acinetobacter baumannii* و *Klebsiella pneumoniae*) یا ژن *mecA* (در MRSA).
   * ایجاد DSB در کروموزوم باکتری باعث مرگ سریع سلول باکتری مقاوم می‌شود (زیرا باکتری‌ها سیستم ترمیم NHEJ کارآمد ندارند).
2. **حذف پلاسمیدهای مقاومت (Plasmid Curing):**
   * هدف‌گیری اوریجین تکثیر یا ژن‌های مقاومت موجود روی پلاسمیدهای R.
   * برش پلاسمید باعث نابودی آن شده و باکتری را مجدداً به آنتی‌بیوتیک‌ها **حساس (Re-sensitized)** می‌سازد.
3. **حامل‌های انتقال (Delivery Vehicles):**
   * استفاده از **Phagemid (فاژهای نوترکیب)** یا **پارتیکل‌های غیرعفونی شبه‌ویروسی (VLP)** برای تزریق CRISPR-Cas9 مستقیماً به باکتری‌های هدف در بدن بیمار.

---

### ۴.۲. غلبه بر مقاومت دارویی در سرطان
* **غربالگری کل ژنوم (Genome-wide CRISPR Screens):**
  استفاده از کتابخانه‌های CRISPRko برای خاموش کردن تک‌تک ژن‌های سلول سرطانی مقاوم به شیمی‌درمانی جهت شناسایی ژن‌های مسئول مقاومت (مثل پمپ‌های خروج داروی ABC Transporters).
* **سرکوب پمپ‌های MDR1 با CRISPRi:**
  کاهش بیان ژن‌های پمپ خروج دارو جهت بقای داروهای شیمی‌درمانی درون سلول سرطانی.

</details>

<details>
<summary><b>فصل ۵: منابع علمی، کتاب‌ها و فیلم‌های آموزشی پیشنهادی</b></summary>

### کتاب‌ها و مقالات مرور تخصصی (Review Papers & Textbooks)
1. **Doudna, J. A., & Charpentier, E. (2014).** *The new frontier of genome engineering with CRISPR-Cas9.* **Science**, 346(6213).
2. **Knott, G. J., & Doudna, J. A. (2018).** *CRISPR-Cas guide RNAs: sky's the limit.* **Nature Structural & Molecular Biology**, 25(4), 247-259.
3. **Gootenberg, J. S., et al. (2017).** *Nucleic acid detection with CRISPR-Cas13a/C2c2.* **Science**, 356(6336), 438-442. (مقاله اصلی تکنولوژی SHERLOCK)
4. **Chen, J. S., et al. (2018).** *CRISPR-Cas12a target binding unleashes indiscriminate single-stranded DNase activity.* **Science**, 360(6387), 436-439. (مقاله اصلی DETECTR)
5. **Pursey, E., et al. (2018).** *CRISPR-Cas antimicrobials: defining the magnitude of resistance.* **Trends in Microbiology**, 26(12), 1005-1016.

---

### فیلم‌ها و دوره‌های ویدئویی آموزشی (Video Lectures & Animations)
1. **Nature Video:** *CRISPR: A gene-editing revolution* (یوتیوب - انیمیشن فوق‌العاده مکانیسم Cas9).
2. **MIT CBMM:** *Genome Editing with CRISPR-Cas9 by Prof. Feng Zhang* (یوتیوب - سخنرانی جامع فنگ ژانگ).
3. **iBiology:** *Jennifer Doudna: Genome Engineering with CRISPR-Cas9* (یوتیوب - تدریس جنیفر داودنا).
4. **Bozeman Science:** *CRISPR-Cas9 Gene Editing* (آموزش مفهومی و بیولوژی پایه).
5. **McGovern Institute:** *How CRISPR-Cas13 & SHERLOCK Work for Viral/Bacterial Diagnostics* (انیمیشن تشخیصی).

</details>