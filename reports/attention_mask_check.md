# Attention / Padding Mask Check

Source: `02_attention_transformers.ipynb`

- Model: `distilbert/distilbert-base-multilingual-cased`
- Hidden state shape: `(2, 10, 768)`
- Attention tensor: `(2, 12, 10, 10)`
- Arabic tokens: `[CLS], ال, ##خدمة, لم, ت, ##ت, ##أ, ##خر, ., [SEP]`
- Row-sum range: `0.9999998211860657` to `1.0`
- `masked_positions_zero`: PASS
- `actual_forward`: PASS

## Architecture
Input → Embedding → Transformer Encoder → Task Head.

## Interpretation limitation
Attention weights are an internal weighting mechanism and should not be
presented as causal explanations of a prediction.
