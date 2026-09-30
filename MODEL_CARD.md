# MODEL_CARD

## Model

Project: Bayan — Applied NLP  
Owner: Haya Albaqami

## Intended use

Educational Arabic/English NLP experimentation covering classification, NER, QA, semantic search and serving.

## Evidence status

The supplied notebooks contain course-fixture and smoke measurements. A final project model card must identify the actual project checkpoint, training data, split, preprocessing version, tokenizer, training configuration and evaluation results.

## Current smoke artefacts

- Classification: `distilbert/distilbert-base-multilingual-cased`
- Arabic comparison: `distilbert/distilbert-base-multilingual-cased` vs `CAMeL-Lab/bert-base-arabic-camelbert-da`
- Search: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- Reranker: `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`

## Limitations

The data are small/educational fixtures and the training runs are short. Results must not be interpreted as production estimates.

## Ethical / privacy notes

Mask supported PII before logging. Do not publish private weights, secrets or raw personal data. Review the model separately before any consequential use.
