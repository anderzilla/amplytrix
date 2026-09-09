# Data classification

| Class        | Examples                                                                  | Handling                                                                         |
| ------------ | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Public       | published catalog/marketing                                               | integrity controls; approved publication                                         |
| Internal     | architecture, redacted dogfood records, telemetry aggregates              | authenticated access; project segregation; limited sharing                       |
| Confidential | customer code/prompts, project sources/evidence, account/billing metadata | encryption, project/tenant authorization, minimized logs, retention/deletion     |
| Restricted   | credentials, tokens, payment/auth secrets, sensitive personal data        | vault only, least privilege, no prompt/log/Git, audited access, rapid revocation |

Owners assign class at schema/contract review. Unknown data defaults to Confidential; credentials always Restricted.

Default retention for Confidential and Restricted project/client data is 90 days after project
closure or contract termination, then deletion or irreversible, validated anonymization — see
`docs/security/lgpd-readiness.md#closure-export-retention-and-deletion` for the full closure
procedure and its exceptions.
