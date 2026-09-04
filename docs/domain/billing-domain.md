# Billing and subscriptions domain

Canonical states: `pending`, `incomplete`, `trialing`, `active`, `past_due`, `grace_period`, `paused`, `cancel_scheduled`, `canceled`, `expired`, `unpaid`. Provider ACLs translate external states; the provider is authoritative for payment facts while Amplytrix owns entitlements, credits and access.

Each transition records previous state, event/preconditions, new state, financial effect, entitlement/credit effect, notification, audit and compensation. Supported lifecycle covers create/activate/trial/convert/renew/fail/recover/upgrade/downgrade/cycle/proration/pause/resume/cancel/expire/reactivate/refund/chargeback/dispute/price migration/founder benefit. Unknown or out-of-order events trigger reconciliation, not guessed transitions.
