from dataclasses import dataclass
from uuid import uuid4

from amplytrix.shared.domain import AggregateRoot, DomainEvent, EntityId, ValueObject


@dataclass(frozen=True, slots=True)
class Label(ValueObject):
    value: str


@dataclass(eq=False, slots=True)
class ExampleAggregate(AggregateRoot):
    pass


def test_value_object_compares_by_value() -> None:
    assert Label("architecture") == Label("architecture")


def test_aggregate_releases_recorded_events_once() -> None:
    aggregate = ExampleAggregate(EntityId(uuid4()))
    event = DomainEvent.occurred_now()
    aggregate.record(event)
    assert aggregate.pull_domain_events() == (event,)
    assert aggregate.pull_domain_events() == ()
