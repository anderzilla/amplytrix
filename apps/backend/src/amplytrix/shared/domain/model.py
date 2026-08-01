from abc import ABC
from dataclasses import dataclass, field
from typing import NewType
from uuid import UUID

from amplytrix.shared.domain.events import DomainEvent

EntityId = NewType("EntityId", UUID)


@dataclass(frozen=True, slots=True)
class ValueObject:
    """Value objects compare by immutable attributes and enforce their own invariants."""


@dataclass(eq=False, slots=True)
class Entity(ABC):
    id: EntityId

    def __eq__(self, other: object) -> bool:
        return isinstance(other, type(self)) and self.id == other.id

    def __hash__(self) -> int:
        return hash((type(self), self.id))


@dataclass(eq=False, slots=True)
class AggregateRoot(Entity, ABC):
    _domain_events: list[DomainEvent] = field(
        default_factory=lambda: list[DomainEvent](), init=False, repr=False
    )

    def record(self, event: DomainEvent) -> None:
        self._domain_events.append(event)

    def pull_domain_events(self) -> tuple[DomainEvent, ...]:
        events = tuple(self._domain_events)
        self._domain_events.clear()
        return events
