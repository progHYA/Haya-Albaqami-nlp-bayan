# بيان — Bayan Bilingual Applied NLP Project | مشروع بيان لمعالجة اللغة ثنائي اللغة

- **Learner:** Haya Albaqami — هياء البقمي
- **GitHub:** https://github.com/progHYA/Haya-Albaqami-nlp-bayan
- **Final release:** `submission-v1.0`

## Executive Summary | الملخص

مشروع بيان هو خط معالجة لغة طبيعية ثنائي اللغة للعربية والإنجليزية، مع التركيز على النصوص العربية القصيرة واللهجة الخليجية في سياق الخدمات الرقمية.

يبدأ الخط بمعالجة النص وTokenization، ثم Transformer/Attention، وتصنيف النص، وNER، وExtractive QA مع حالة no-answer، ثم البحث الدلالي وإعادة الترتيب، والتقييم وتحليل الأخطاء، وأخيرًا القياس والخدمة.

**البيانات تعليمية/اصطناعية وصغيرة**؛ لذلك لا تمثل النتائج أداءً إنتاجيًا على بيانات مستفيدين حقيقيين.

## What Bayan Does | ماذا يفعل بيان؟

1. **Preprocessing:** معالجة النص العربي والإنجليزي قبل إدخاله للنموذج.
2. **Tokenization:** فحص fertility وtruncation وأساليب الترميز.
3. **Attention & Transformers:** فحص Transformer Encoder وQ/K/V والأقنعة.
4. **Classification:** تصنيف النص باستخدام Transformer مع baseline.
5. **NER:** استخراج الكيانات ومحاذاة BIO وتقييم Entity-F1.
6. **QA:** إجابة استخراجية من السياق مع حالة no-answer.
7. **Semantic Search:** بحث دلالي باستخدام embeddings وFAISS مع reranking.
8. **Evaluation:** مقاييس، شرائح، فترات ثقة، وتحليل أخطاء.
9. **Optimization & Serving:** قياس الأداء وONNX/INT8 واختبارات الخدمة.

## Scope and Limitations | النطاق والحدود

- المشروع تعليمي ومبني على بيانات صغيرة.
- النتائج لا تمثل أداءً إنتاجيًا.
- حجم عينات الاختبار صغير، لذلك يجب تفسير النتائج وفترات الثقة بحذر.
- لا ينبغي استخدام النموذج لاتخاذ قرارات عالية المخاطر عن أشخاص حقيقيين دون تحقق إضافي ومراجعة بشرية.

## Reproduce | إعادة التشغيل

| # | Notebook | Purpose | Evidence |
|---:|---|---|---|
| 00 | `00_runtime_doctor.ipynb` | فحص البيئة | `notebooks/` |
| 01 | `01_text_processing_tokenization.ipynb` | preprocessing وtokenization | `notebooks/` + `reports/` |
| 02 | `02_attention_transformers.ipynb` | attention وTransformer | `notebooks/` + `reports/` |
| 03 | `03_text_classification.ipynb` | classification | `notebooks/` + `reports/` |
| 04 | `04_ner_and_qa.ipynb` | NER وQA | `notebooks/` + `reports/` |
| 05 | `05_arabic_nlp.ipynb` | Arabic NLP | `notebooks/` + `reports/` |
| 06 | `06_semantic_search.ipynb` | semantic search + reranking | `notebooks/` + `reports/` |
| 07 | `07_evaluation_error_analysis.ipynb` | evaluation + error analysis | `notebooks/` + `reports/` |
| 08 | `08_optimization_serving.ipynb` | benchmark + optimization + serving | `notebooks/` + `reports/` |

يفضل تشغيل الدفاتر بالترتيب **00 → 08** وحفظ النسخ المنفذة داخل `notebooks/`.

### Tests and validation

```bash
pip install -r requirements-dev.txt
PYTHONPATH=src python -m pytest -q tests
python scripts/validate_submission.py . --json-report reports/submission_validation.json
python scripts/preflight_submission.py . --report reports/preflight.json
```

> لا تُعتبر نتائج الاختبارات أو تقارير الفحص نهائية إلا إذا كانت الملفات الناتجة محفوظة في `reports/` من التشغيل الفعلي.

## Architecture | المعمارية

```text
Arabic / English text
        |
        v
Preprocessing + Tokenization
        |
        v
Transformer Encoder
        |
   +----+----+----+
   |    |    |    |
   v    v    v    v
Class  NER   QA  Search
              |     |
              |     v
              |   FAISS
              |     |
              |  Reranking
              +-----+
                    |
                    v
        Evaluation + Serving
```

### Attention interpretation

مسار الـTransformer يستخدم self-attention مع masks مناسبة. أوزان attention تصف ما يحسبه رأس attention، لكنها لا تُعامل وحدها كتفسير سببي لقرار النموذج؛ لأن التمثيلات تمر أيضًا عبر residual connections وfeed-forward layers وطبقات أخرى.

## Results | النتائج

> **ملاحظة مهمة:** الأرقام أدناه هي الأرقام التي كانت متاحة في ملفات المشروع السابقة، وبعضها موسوم `MEASURED_SMOKE` أو `COURSE_FIXTURE`. لا ينبغي وصفها بأنها نتائج PROJECT_ARTIFACT إلا إذا كان تقرير التشغيل الأخير يؤكد ذلك.

| Component | Metric | Available result | Evidence |
|---|---|---:|---|
| Classification | Test Macro-F1 | 0.867 `MEASURED_SMOKE` | `reports/classification_results.json` |
| Classification | Test accuracy | 0.875 `MEASURED_SMOKE` | `reports/classification_results.json` |
| NER | Entity-F1 | 0.571 `MEASURED_SMOKE` | `reports/ner_results.json` |
| QA | Valid span example | `الرياض` `MEASURED_SMOKE` | `reports/qa_results.json` |
| QA | No-answer test | PASS `MEASURED_SMOKE` | `reports/qa_results.json` |
| Search | Recall@3 | 1.000 `MEASURED_SMOKE` | `reports/search_results.json` |
| Search | MRR@3 before rerank | 0.667 `MEASURED_SMOKE` | `reports/search_results.json` |
| Search | MRR@3 after rerank | 0.722 `MEASURED_SMOKE` | `reports/search_results.json` |
| Search | MRR@3 delta | +0.056 `MEASURED_SMOKE` | `reports/search_results.json` |
| Evaluation | Macro-F1 estimate | 0.7819 `COURSE_FIXTURE` | `reports/evaluation_report.json` |
| Evaluation | Bootstrap 95% CI | [0.6112, 0.8962] `COURSE_FIXTURE` | `reports/evaluation_report.json` |
| Serving | Arabic/English smoke | PASS `MEASURED_SMOKE` | `reports/serving_project_results.json` |
| Serving | Empty input | 422 `MEASURED_SMOKE` | `reports/serving_project_results.json` |
| Serving | Unsupported language | 422 `MEASURED_SMOKE` | `reports/serving_project_results.json` |

### Benchmark evidence

القياسات المتاحة سابقًا كانت مع `PROJECT_MODE=False`، لذلك لا تُعرض كأداء نهائي لنموذج المشروع حتى يتم التحقق من تشغيل Notebook 08 على artifact المشروع.

- PyTorch p95: **43.977 ms**
- ONNX FP32 p95: **27.258 ms**
- ONNX INT8 p95: **11.916 ms**
- FP32 prediction agreement: **1.00**
- INT8 prediction agreement: **0.75**

## Error Analysis | تحليل الأخطاء

التحليل المتاح سابقًا صنّف الحالات إلى:

- `dialect_gap`: 3
- `hard_or_ambiguous`: 3
- `class_confusion`: 2

الإصلاحات المقترحة:

1. إضافة أمثلة خليجية مستهدفة للصحة والنقل.
2. إضافة أمثلة contrastive للعبارات المتشابهة ومراجعة دليل التسميات.
3. طلب سياق إضافي أو abstain عند انخفاض الثقة في الطلبات القصيرة غير المحددة.

> لا تُوصف هذه الأعداد بأنها أخطاء نموذج المشروع النهائي إلا إذا أكدها تشغيل Notebook 07 الأخير.

## Repository Evidence | أدلة المستودع

- `notebooks/` — دفاتر المشروع 00–08.
- `reports/` — التقارير والنتائج.
- `src/bayan/` — كود المشروع.
- `tests/` — الاختبارات.
- `docs/` — التوثيق.
- `evidence/` — الأدلة الداعمة.
- `BENCHMARKS.md`
- `DECISIONS.md`
- `EVALUATION_REPORT.md`
- `MODEL_CARD.md`
- `DATA_CARD.md`
- `PROGRESS.md`
- `STUDENT_PROFILE.md`
- `PRESENTATION.md`
- `PROJECT_SUMMARY.json`
- `SUBMISSION.yml`

## Release | الإصدار

- **Repository:** `https://github.com/progHYA/Haya-Albaqami-nlp-bayan`
- **Release:** `submission-v1.0`

## Contribution | مساهمتي

تم تنظيم مكونات المشروع، تشغيل الدفاتر، حفظ التقارير والأدلة، وتجهيز المستودع للتقييم النهائي ضمن سياق مشروع Applied NLP.

## AI Assistance | الاستعانة بالذكاء الاصطناعي

تم استخدام أدوات ذكاء اصطناعي للمساعدة في تنظيم الملفات، صياغة بعض التوثيق، ومراجعة متطلبات التقييم. تمت مراجعة المحتوى والنتائج قبل حفظ النسخة النهائية.

> إذا كان التقييم يطلب اسم الأداة تحديدًا، اكتبي اسم الأداة المستخدمة فعليًا بدل هذا السطر العام.

## Responsible Use | الاستخدام المسؤول

المشروع تعليمي، والبيانات صغيرة ومحدودة. لا ينبغي استخدام النظام لاتخاذ قرارات عن أشخاص حقيقيين دون مراجعة بشرية وتحقيق إضافي في الأداء والسلامة.

## Final Validation | الفحص النهائي

يُفضّل حفظ مخرجات الفحص داخل `reports/`:

```text
reports/submission_validation.json
reports/preflight.json
```

ويجب أن يشير `submission-v1.0` إلى الـcommit النهائي الذي يحتوي على الدفاتر والتقارير والاختبارات.

## Training Context | السياق التدريبي

هذا المشروع التعليمي أُنجز ضمن سياق التدريب على معالجة اللغات الطبيعية باستخدام Transformers في أكاديمية سدايا.

#SDAIAAcademy
