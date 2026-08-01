# Multi-tenancy

Organization is the tenant boundary; personal organizations avoid user-special cases. Tenant-owned rows carry non-null `organization_id`; compound unique/index/FK design includes it where it prevents cross-tenant references. Repositories require explicit tenant scope from authenticated context, never caller-controlled filters. Authorization and data-leak tests cover list, detail, export, invoice, artifact and admin paths.

PostgreSQL RLS is defense-in-depth to benchmark before activation: it improves enforcement but introduces session-context, migration, pooling and operational complexity. Application deny-default authorization remains mandatory. Database-per-tenant, regional databases and sharding require measured isolation/scale evidence.
