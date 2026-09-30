# Evaluation Report — Bayan

## Evidence scope

This report is reconstructed from the supplied notebooks and the 2026-09-30 evaluation sheet. It deliberately distinguishes course-fixture/smoke measurements from missing project-artifact evidence.

## Classification

- Validation Macro-F1 baseline: **0.6667**
- Validation Macro-F1 Transformer: **1.0000**
- Validation delta: **+0.3333**
- Test Macro-F1 Transformer: **0.8667**
- Test accuracy Transformer: **0.8750**

Dataset: 40 course-fixture rows; train 24, validation 8, test 8; 20 groups; group overlap 0.

## NER / QA

NER smoke:

- entity precision: 0.6667
- entity recall: 0.5000
- entity F1: 0.5714
- true entities: 4
- predicted entities: 3

QA smoke:

- optimizer steps: 3
- mean loss: 3.6451
- valid-span test returned `الرياض`
- no-answer test returned no answer with margin 6.0

These are smoke tests, not production quality estimates.

## Semantic search

- corpus vectors: 24
- embedding dimension: 384
- Recall@3: 1.0000
- MRR@3: 0.6667
- cross-lingual slice Recall@3: 1.0000, n=2
- reranked MRR@3: 0.7222
- reranking delta: +0.0556
- threshold validation accuracy: 1.0000
- frozen test no-answer accuracy: 1.0000

## Evaluation fixture

Macro-F1 fixture:

- estimate: 0.7819
- 95% bootstrap CI: 0.6112–0.8962
- paired B−A difference: +0.0012
- paired 95% CI: −0.1047–0.0996

The paired interval includes zero, so the supplied fixture does not support a directional superiority claim.

Slices included Arabic, English, Gulf, MSA, English variant, and short/long length buckets. Small slices were explicitly flagged.

## Error taxonomy

Course fixture only:

| Category | Count |
|---|---:|
| dialect_gap | 3 |
| hard_or_ambiguous | 3 |
| class_confusion | 2 |

The final project report must replace these with manually reviewed errors from the student's actual model.

## Missing final evidence

The evaluation requires:

- project-specific Macro-F1/entity-F1/no-answer metrics
- project semantic-search reports before/after reranking
- project error examples and three fixes
- completed model/data cards
- project benchmark with p50/p95/p99, throughput, memory and quality tax
- project ONNX/INT8 decision
- measured extension
- validator/preflight reports
