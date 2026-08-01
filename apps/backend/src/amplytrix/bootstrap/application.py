from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI

from amplytrix.bootstrap.settings import get_settings
from amplytrix.shared.presentation.http.health import router as health_router
from amplytrix.shared.presentation.http.middleware import CorrelationIdMiddleware


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:
    yield


def create_application() -> FastAPI:
    settings = get_settings()
    structlog.configure(processors=[structlog.processors.JSONRenderer()])
    application = FastAPI(
        title="Amplytrix API",
        version="0.0.0",
        docs_url=None if settings.environment == "production" else "/docs",
        redoc_url=None,
        lifespan=lifespan,
    )
    application.add_middleware(CorrelationIdMiddleware)
    application.include_router(health_router)
    return application
