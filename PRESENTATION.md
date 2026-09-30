# PRESENTATION

## Slide 1 — Bayan Applied NLP
Haya Albaqami — Applied NLP project.

## Slide 2 — Pipeline
Arabic/English text → privacy/preprocessing → tokenization/embeddings → task models → evaluation → optimized serving.

## Slide 3 — Current measured evidence
Classification, NER/QA, semantic search and systems benchmarks are currently documented as course-fixture/smoke evidence.

## Slide 4 — Arabic NLP
Named preprocessing profile, PII masking, conservative display/model separation, and model comparison smoke.

## Slide 5 — Semantic search
FAISS retrieval with multilingual embeddings, thresholding and reranking. Smoke MRR improved from 0.6667 to 0.7222.

## Slide 6 — Evaluation
Bootstrap confidence intervals, paired comparison, slices and behavioural tests are implemented.

## Slide 7 — Serving
ONNX FP32 parity passed; INT8 reduced p95 latency in the smoke workload but had 0.75 prediction agreement, so it did not meet the smoke quality budget.

## Slide 8 — Finalization
Project-specific reruns, error analysis, Gate D benchmark and submission validation are still required.
