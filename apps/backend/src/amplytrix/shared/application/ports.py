from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class ModelRequest:
    prompt: str


@dataclass(frozen=True, slots=True)
class ModelResponse:
    text: str
    input_tokens: int
    output_tokens: int


class LanguageModelGateway(Protocol):
    async def generate(self, request: ModelRequest) -> ModelResponse: ...


class EmbeddingGateway(Protocol):
    async def embed(self, texts: list[str]) -> list[list[float]]: ...


class UnitOfWork(Protocol):
    async def __aenter__(self) -> "UnitOfWork": ...
    async def __aexit__(self, exc_type: object, exc: object, traceback: object) -> None: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
