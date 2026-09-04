from amplytrix.catalog.infrastructure.seeds import (
    FEATURE_SEEDS,
    PLAN_SEEDS,
    PRICE_HYPOTHESIS_SEEDS,
    PRODUCT_SEED,
)


def test_required_plan_and_product_seeds_exist() -> None:
    assert PRODUCT_SEED["code"] == "amplytrix"
    assert {plan.code for plan in PLAN_SEEDS} == {
        "free",
        "pro_trial",
        "pro",
        "team",
        "premium_architecture",
    }


def test_example_prices_are_hypotheses_and_use_minor_units() -> None:
    assert all(isinstance(seed["amount_minor"], int) for seed in PRICE_HYPOTHESIS_SEEDS)
    assert all(seed["currency"] == "BRL" for seed in PRICE_HYPOTHESIS_SEEDS)


def test_core_feature_seeds_cover_commercial_grants() -> None:
    assert {"workspace", "ask_project", "monthly_credits", "audit"} <= set(FEATURE_SEEDS)
