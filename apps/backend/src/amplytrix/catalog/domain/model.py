from dataclasses import dataclass, field
from enum import StrEnum
from uuid import UUID


class CatalogStatus(StrEnum):
    DRAFT = "draft"
    PUBLISHED = "published"
    RETIRED = "retired"


class CommercialVisibility(StrEnum):
    INTERNAL = "internal"
    FREE = "free"
    TRIAL = "trial"
    PAID = "paid"
    PREMIUM = "premium"
    INVITE_ONLY = "invite_only"
    DEPRECATED = "deprecated"


@dataclass(frozen=True, slots=True, order=True)
class SemanticVersion:
    major: int
    minor: int
    patch: int

    def __post_init__(self) -> None:
        if min(self.major, self.minor, self.patch) < 0:
            raise ValueError("semantic version components cannot be negative")

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"


@dataclass(frozen=True, slots=True)
class Money:
    minor_units: int
    currency: str

    def __post_init__(self) -> None:
        if self.minor_units < 0:
            raise ValueError("money cannot be negative")
        if len(self.currency) != 3 or not self.currency.isalpha():
            raise ValueError("currency must be a three-letter ISO code")
        object.__setattr__(self, "currency", self.currency.upper())


@dataclass(frozen=True, slots=True)
class Product:
    id: UUID
    code: str
    name: str


@dataclass(frozen=True, slots=True)
class Feature:
    id: UUID
    code: str
    name: str


@dataclass(frozen=True, slots=True)
class PlanLimit:
    feature_code: str
    value: int
    unit: str

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("plan limit cannot be negative")


@dataclass(frozen=True, slots=True)
class CatalogItemVersion:
    id: UUID
    version: SemanticVersion
    name: str
    short_description: str
    commercial_description: str
    visibility: CommercialVisibility
    status: CatalogStatus = CatalogStatus.DRAFT

    def publish(self) -> "CatalogItemVersion":
        if self.status is not CatalogStatus.DRAFT:
            raise ValueError("only a draft catalog item version can be published")
        return CatalogItemVersion(
            id=self.id,
            version=self.version,
            name=self.name,
            short_description=self.short_description,
            commercial_description=self.commercial_description,
            visibility=self.visibility,
            status=CatalogStatus.PUBLISHED,
        )


@dataclass(slots=True)
class CatalogItem:
    id: UUID
    code: str
    slug: str
    versions: list[CatalogItemVersion] = field(default_factory=lambda: list[CatalogItemVersion]())

    def add_version(self, candidate: CatalogItemVersion) -> None:
        if any(item.version == candidate.version for item in self.versions):
            raise ValueError("catalog item version already exists")
        if self.versions and candidate.version <= max(item.version for item in self.versions):
            raise ValueError("catalog item versions must increase")
        self.versions.append(candidate)

    def public_version(self) -> CatalogItemVersion | None:
        visible = [
            item
            for item in self.versions
            if item.status is CatalogStatus.PUBLISHED
            and item.visibility
            not in {CommercialVisibility.INTERNAL, CommercialVisibility.DEPRECATED}
        ]
        return max(visible, key=lambda item: item.version, default=None)


@dataclass(frozen=True, slots=True)
class PlanVersion:
    id: UUID
    version: SemanticVersion
    status: CatalogStatus
    feature_codes: frozenset[str]
    limits: tuple[PlanLimit, ...]


@dataclass(slots=True)
class Plan:
    id: UUID
    code: str
    slug: str
    versions: list[PlanVersion] = field(default_factory=lambda: list[PlanVersion]())

    def add_version(self, candidate: PlanVersion) -> None:
        if any(item.version == candidate.version for item in self.versions):
            raise ValueError("plan version already exists")
        if self.versions and candidate.version <= max(item.version for item in self.versions):
            raise ValueError("plan versions must increase")
        self.versions.append(candidate)


@dataclass(frozen=True, slots=True)
class Price:
    id: UUID
    plan_version_id: UUID
    amount: Money
    billing_period: str
    hypothesis: bool
    status: CatalogStatus = CatalogStatus.DRAFT

    def publish(self) -> "Price":
        if not self.hypothesis:
            raise ValueError("pricing requires an explicitly reviewed hypothesis")
        if self.status is not CatalogStatus.DRAFT:
            raise ValueError("only a draft price can be published")
        return Price(
            id=self.id,
            plan_version_id=self.plan_version_id,
            amount=self.amount,
            billing_period=self.billing_period,
            hypothesis=self.hypothesis,
            status=CatalogStatus.PUBLISHED,
        )


@dataclass(frozen=True, slots=True)
class AddOn:
    id: UUID
    code: str
    name: str
