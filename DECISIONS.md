# DECISIONS — Bayan

## 1. Evidence policy

All metrics are labeled by evidence type:

- `COURSE_FIXTURE`: course fixture, not project performance.
- `MEASURED_SMOKE`: short/smoke run on the course fixture.
- `SYSTEMS_SMOKE`: systems mechanics only; not a quality claim.
- `PROJECT_ARTIFACT`: reserved for a rerun using the student's actual trained model and validation data.

No smoke result is promoted to a project-quality claim.

## 2. Arabic preprocessing

Current smoke profile:

- profile: `search`
- version: `1.0.0`
- backend: `camel-tools==1.6.0`
- preserve display copy
- mask supported PII patterns before logging
- Unicode normalization without compatibility folding
- remove tatweel and diacritics
- fold alef and alef maqsura
- preserve taa marbuta

Golden tests: 4/4 passed in the supplied notebook.

**Project decision still required:** compare the chosen profile against an alternative on the project's own validation data and record the impact by language/variant/task.

## 3. Tokenizer decision

The supplied tokenization smoke run reported mean fertility `1.36` and truncation rate `0%` at length 10 on five synthetic samples.

This is insufficient to choose a project tokenizer. The project run should compare fertility and truncation on the actual Bayan data and record the selected tokenizer plus rationale.

## 4. Attention interpretation

The notebook verifies scaling, masking, multi-head shapes and NumPy/PyTorch parity. README documentation now explicitly states that attention weights are not causal explanations.

## 5. Classification

Smoke run:

- TF-IDF validation Macro-F1: `0.6667`
- Transformer validation Macro-F1: `1.0000`
- Transformer test Macro-F1: `0.8667`
- Transformer test accuracy: `0.8750`

Because the supplied evaluation states these were course-lab outputs, they remain `MEASURED_SMOKE`.

## 6. Semantic search

Smoke run:

- Recall@3: `1.0000`
- MRR@3 before reranking: `0.6667`
- MRR@3 after reranking: `0.7222`
- delta: `+0.0556`
- threshold validation accuracy: `1.0000`
- frozen test no-answer accuracy: `1.0000`

Reranker decision in the smoke notebook: `ADOPT_FOR_EXPERIMENT`.

This is not a final project deployment decision.

## 7. Serving

Systems-smoke benchmark:

- PyTorch p95: `43.977 ms`
- ONNX FP32 p95: `27.258 ms`
- INT8 p95: `11.916 ms`
- FP32 ONNX prediction agreement: `1.0`
- INT8 agreement: `0.75`

The smoke budget selected ONNX FP32 for service mechanics, but the notebook explicitly says this is not a shipping decision.

**Project decision still required:** rerun with `PROJECT_MODE=True`, project artefact, full workload and student-defined budget, then record Adopt/Reject/Rollback.

## 8. Error analysis

The course fixture produced:

- `dialect_gap`: 3
- `hard_or_ambiguous`: 3
- `class_confusion`: 2

The supplied evaluation requires these categories to be derived from the student's own model errors. Therefore these counts are not presented as Haya's final error distribution.

## 9. Extension

A project-specific extension must be measured against baseline. The current repository does not contain sufficient evidence to claim a measured extension benefit. Do not invent one.

