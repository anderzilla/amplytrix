# CodeMatrix collaboration authority

Amplytrix adopts the following governance references without copying credentials, personal data, or
operational records from the private CodeMatrix Blueprint.

| Reference         | Canonical location                                                          | Verified commit                            | Applied invariant                                                                                |
| ----------------- | --------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| RULE-034          | `knowledge/records/rules.jsonl` in `anderzilla/CodeMatrixInternacional`     | `3ab73de9c65d0f1be0177b293dab6cbaf710e29b` | every AI delivery has a traceable primary owner and independent reviewer                         |
| DEC-035           | `knowledge/records/decisions.jsonl` in `anderzilla/CodeMatrixInternacional` | `3ab73de9c65d0f1be0177b293dab6cbaf710e29b` | proportional multi-AI collaboration is mandatory; missing review keeps work draft/blocked        |
| Portable protocol | `docs/06-operating-model/MULTI_AI_PORTFOLIO_ORCHESTRATION.md`               | `3ab73de9c65d0f1be0177b293dab6cbaf710e29b` | linked envelopes/evidence, contrary evidence, cost, stop conditions, evidence-based adjudication |

The governance commit is a provenance anchor, not an authorization token. Amplytrix records its own
task artifacts under the project package. A reviewer is read-only whenever possible and must review
the exact proposed commit. Deterministic validation complements but never impersonates independent
review. A pull request does not authorize merge, deployment, production access, financial action, or
contractual acceptance.
