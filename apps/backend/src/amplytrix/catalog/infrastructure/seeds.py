from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PlanSeed:
    code: str
    slug: str
    name: str


PRODUCT_SEED = {"code": "amplytrix", "name": "Amplytrix"}

PLAN_SEEDS = (
    PlanSeed("free", "free", "Free"),
    PlanSeed("pro_trial", "pro-trial", "Pro Trial"),
    PlanSeed("pro", "pro", "Pro"),
    PlanSeed("team", "team", "Team"),
    PlanSeed("premium_architecture", "premium-architecture", "Premium Architecture"),
)

FEATURE_SEEDS = (
    "workspace",
    "repository",
    "ask_project",
    "monthly_credits",
    "technical_memory",
    "living_documentation",
    "collaboration",
    "audit",
    "impact_analysis",
    "custom_agents",
)

# These are explicitly non-final examples for local/sandbox validation only.
PRICE_HYPOTHESIS_SEEDS = (
    {"plan": "free", "amount_minor": 0, "currency": "BRL", "period": "month"},
    {"plan": "pro", "amount_minor": 9900, "currency": "BRL", "period": "month"},
    {"plan": "team", "amount_minor": 29900, "currency": "BRL", "period": "month"},
    {
        "plan": "premium_architecture",
        "amount_minor": 99900,
        "currency": "BRL",
        "period": "month",
    },
)
