from fastapi import APIRouter

from amplytrix.shared.presentation.http.schemas import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health/live", response_model=HealthResponse, operation_id="getLiveness")
async def liveness() -> HealthResponse:
    return HealthResponse(status="ok", service="backend")


@router.get("/health/ready", response_model=HealthResponse, operation_id="getReadiness")
async def readiness() -> HealthResponse:
    return HealthResponse(status="ready", service="backend")
