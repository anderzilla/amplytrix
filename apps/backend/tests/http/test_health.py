from typing import cast

from fastapi.testclient import TestClient
from httpx import Response

from amplytrix.bootstrap.application import create_application


def test_health_and_readiness_contracts() -> None:
    client = TestClient(create_application())
    # Starlette's TestClient currently loses httpx return types under strict Pyright.
    live = cast(Response, client.get("/health/live"))  # pyright: ignore[reportUnknownMemberType]
    ready = cast(Response, client.get("/health/ready"))  # pyright: ignore[reportUnknownMemberType]
    assert live.status_code == 200
    assert cast(dict[str, str], live.json()) == {"status": "ok", "service": "backend"}
    assert ready.status_code == 200
    assert cast(dict[str, str], ready.json()) == {"status": "ready", "service": "backend"}
    assert live.headers["x-correlation-id"]


def test_invalid_correlation_id_is_not_reflected() -> None:
    client = TestClient(create_application())
    response = cast(
        Response,
        client.get(  # pyright: ignore[reportUnknownMemberType]
            "/health/live", headers={"x-correlation-id": "not-a-uuid"}
        ),
    )
    assert response.headers["x-correlation-id"] != "not-a-uuid"
