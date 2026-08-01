import ast
from pathlib import Path

FORBIDDEN_DOMAIN_IMPORTS = {"fastapi", "pydantic", "sqlalchemy", "alembic", "asyncpg"}


def imported_roots(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".")[0])
    return roots


def test_domain_has_no_framework_dependencies() -> None:
    domain = Path("src/amplytrix/shared/domain")
    violations = {
        str(path): imported_roots(path) & FORBIDDEN_DOMAIN_IMPORTS
        for path in domain.glob("*.py")
        if imported_roots(path) & FORBIDDEN_DOMAIN_IMPORTS
    }
    assert violations == {}


def test_application_does_not_import_outer_layers() -> None:
    application = Path("src/amplytrix/shared/application")
    forbidden = {"amplytrix.shared.infrastructure", "amplytrix.shared.presentation"}
    violations: dict[str, set[str]] = {}
    for path in application.glob("*.py"):
        source = path.read_text(encoding="utf-8")
        imports = {
            node.module
            for node in ast.walk(ast.parse(source))
            if isinstance(node, ast.ImportFrom) and node.module
        }
        found = {name for name in imports if any(name.startswith(item) for item in forbidden)}
        if found:
            violations[str(path)] = found
    assert violations == {}
