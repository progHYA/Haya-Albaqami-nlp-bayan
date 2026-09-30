# Tokenizer Decision

## Evidence available from the supplied notebook
`01_text_processing_tokenization.ipynb` reports an mBERT tokenization example with
12 tokens and confirms that the fast tokenizer is enabled.

## Limitation
The supplied notebook output does **not** contain a full two-tokenizer comparison
over the Bayan corpus with fertility and truncation percentages. Therefore this
file does not claim that such a corpus-level comparison was completed.

## Decision
Use the fast tokenizer implementation already exercised in the notebook for the
measured smoke pipeline; a full corpus-level tokenizer decision remains a
project-specific follow-up if required by the evaluator.
