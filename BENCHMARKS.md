# BENCHMARKS

## Systems smoke benchmark

| Candidate | p95 model-only | Size | Quality/parity | Status |
|---|---:|---:|---:|---|
| PyTorch | 43.977 ms | 16.732 MiB parameters | reference | baseline |
| ONNX FP32 | 27.258 ms | 16.788 MiB | prediction agreement 1.0 | smoke-selected |
| ONNX INT8 | 11.916 ms | 4.287 MiB | agreement 0.75 vs FP32 | budget failed |

Workload: 8 bilingual rows, CPU, warmup 5, repetitions 30, max length 96, batch size 4.

**Important:** this is `SYSTEMS_SMOKE`. It is not a project quality benchmark and not a final shipping decision.

## Gate D rerun required

Set:

```text
PROJECT_MODE=True
PROJECT_MODEL_SOURCE=<project checkpoint>
PROJECT_TOKENIZER_SOURCE=<project tokenizer>
PROJECT_VALIDATION_CSV=<full bilingual validation CSV>
BUDGET_PROVENANCE=STUDENT_DEFINED_BEFORE_MEASUREMENT
```

Then record p50/p95/p99, throughput, memory, quality tax, ONNX parity, INT8 parity and Adopt/Reject/Rollback.

