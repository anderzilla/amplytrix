from uuid import UUID, uuid4

from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send

CORRELATION_HEADER = "x-correlation-id"


class CorrelationIdMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self._app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self._app(scope, receive, send)
            return
        headers = dict(scope.get("headers", []))
        raw_value = headers.get(CORRELATION_HEADER.encode("ascii"), b"").decode("ascii", "ignore")
        try:
            correlation_id = str(UUID(raw_value))
        except ValueError:
            correlation_id = str(uuid4())

        async def send_with_correlation(message: Message) -> None:
            if message["type"] == "http.response.start":
                response_headers = MutableHeaders(scope=message)
                response_headers.append(CORRELATION_HEADER, correlation_id)
            await send(message)

        await self._app(scope, receive, send_with_correlation)
