# DATA_CARD

## Dataset role

The supplied notebooks use educational synthetic/course fixtures.

## Current fixture evidence

- Classification: 40 rows, four labels, 20 groups; train 24 / validation 8 / test 8.
- Arabic profile fixture: 20 rows; variants include Gulf, MSA and Arabizi.
- Semantic search: 24 corpus cases and 18 queries.
- Evaluation fixture: 36 rows.
- Systems smoke workload: 8 bilingual rows.

## Data limitations

These are small educational fixtures and are not representative of production traffic or the full diversity of Arabic users.

## Privacy

The preprocessing contract masks supported email/phone patterns before logs. Raw personal data must not be committed.

## Final project requirement

Replace fixture-only claims with the actual project validation/test data and record dataset version/hash and split provenance.
