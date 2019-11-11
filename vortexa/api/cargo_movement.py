from dataclasses import dataclass
from typing import List, Optional

from vortexa.api.geography import GeographyEntity
from vortexa.api.product import ProductEntity
from vortexa.api.shared_types import ISODate, ID
from vortexa.api.vessel import VesselEntity


@dataclass(frozen=True)
class CargoEvent:
    """

    A CargoEvent represents an event that occurred to a cargo during a cargo movement.

    [Cargo Event Entities Further Documentation](https://docs.vortexa.com/reference/intro-cargo-events)

    """

    event_type: str
    location: List[GeographyEntity]

    probability: Optional[float] = None
    pos: Optional[List[float]] = None
    vessel_id: Optional[str] = None
    start_timestamp: Optional[ISODate] = None
    end_timestamp: Optional[ISODate] = None


@dataclass(frozen=True)
class CargoMovement:
    """

    Cargo movements are the base data set the Vortexa API is centred around.

    Each movement represents a journey of a certain quantity of a product between places.

    [Cargo Movement Further Documentation](https://docs.vortexa.com/reference/intro-cargo-movement)

    """

    cargo_movement_id: ID
    quantity: int
    status: str
    vessels: List[VesselEntity]
    product: List[ProductEntity]
    events: List[CargoEvent]
