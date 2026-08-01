# Data classification

| Class        | Examples                                                           | Handling                                                                         |
| ------------ | ------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| Public       | published catalog/marketing                                        | integrity controls; approved publication                                         |
| Internal     | architecture, telemetry aggregates                                 | authenticated access; limited sharing                                            |
| Confidential | customer code/prompts, account/billing metadata                    | encryption, tenant authorization, minimized logs, retention/deletion             |
| Restricted   | credentials, tokens, payment/auth secrets, sensitive personal data | vault only, least privilege, no prompt/log/Git, audited access, rapid revocation |

Owners assign class at schema/contract review. Unknown data defaults to Confidential; credentials always Restricted.
