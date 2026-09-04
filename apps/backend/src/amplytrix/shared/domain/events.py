from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True, kw_only=True)
class DomainEvent:
    event_id: UUID
    occurred_at: datetime

    @classmethod
    def occurred_now(cls) -> "DomainEvent":
        return cls(event_id=uuid4(), occurred_at=datetime.now(UTC))
