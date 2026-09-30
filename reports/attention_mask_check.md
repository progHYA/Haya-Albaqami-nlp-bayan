# Attention / Padding Mask Check

## Architecture trace
Input → Embedding → Encoder layers → Task head

## Project-specific check
**RUN_REQUIRED:** Add one Arabic sentence from the project, its tokenized form,
padding positions, attention mask, and the observed masked/unmasked behavior.

## Interpretation limitation
Attention weights should not be presented as causal explanations of model
predictions. They describe an internal weighting mechanism and do not by
themselves establish that a token caused the prediction.
