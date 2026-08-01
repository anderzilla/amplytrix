from dataclasses import dataclass
from typing import Protocol, TypeVar

ResultT_co = TypeVar("ResultT_co", covariant=True)


@dataclass(frozen=True, slots=True, kw_only=True)
class Command:
    actor_id: str


@dataclass(frozen=True, slots=True, kw_only=True)
class Query:
    actor_id: str


class Handler(Protocol[ResultT_co]):
    async def __call__(self) -> ResultT_co: ...
