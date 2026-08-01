# Secrets responsibility matrix (no values)

| Secret class               | Store          | Runtime accessor           | Owner            | Rotation/revocation               |
| -------------------------- | -------------- | -------------------------- | ---------------- | --------------------------------- |
| Database credential        | Secret Manager | API/worker service account | Platform         | rotate user, revoke IAM/access    |
| Identity provider secret   | Secret Manager | API only                   | Security         | provider console + secret version |
| Payment webhook/API secret | Secret Manager | billing adapter only       | Finance/security | provider revoke/roll keys         |
| AI provider key            | Secret Manager | model adapter only         | AI/platform      | provider revoke + budget lock     |
| Local developer values     | ignored `.env` | named developer            | Developer        | delete/reissue; never share       |
