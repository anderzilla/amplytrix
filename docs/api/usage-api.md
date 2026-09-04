# Usage API (`/api/v1`)

`GET /usage`, `/usage/meters`, `/usage/credits`, `/usage/history` return tenant-scoped aggregates and cursor-paginated ledger views. Records state meter/unit/window, granted/reserved/consumed/remaining and freshness. Raw provider cost and internal abuse signals are restricted.

Execution producers submit usage through an internal authenticated/idempotent application contract; clients cannot post arbitrary billable events. Corrections create compensating ledger entries and audit evidence.
