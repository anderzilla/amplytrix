import json
from pathlib import Path

from amplytrix.bootstrap.application import create_application


def main() -> None:
    target = Path(__file__).parents[3] / "packages" / "api-contracts" / "openapi.json"
    document = create_application().openapi()
    target.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
