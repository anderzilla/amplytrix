from amplytrix.catalog.infrastructure.database import CatalogBase


def test_catalog_metadata_owns_expected_tables_and_schema() -> None:
    assert set(CatalogBase.metadata.tables) == {
        "catalog.products",
        "catalog.catalog_items",
        "catalog.catalog_item_versions",
        "catalog.features",
        "catalog.plans",
        "catalog.plan_versions",
        "catalog.prices",
        "catalog.plan_features",
        "catalog.plan_limits",
        "catalog.add_ons",
    }
    assert all(table.schema == "catalog" for table in CatalogBase.metadata.tables.values())
