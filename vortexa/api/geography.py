from dataclasses import dataclass
from typing import List, Optional

from vortexa.api.shared_types import EntityWithProbability, IDLayer, IDNameLayer, Node, Position


@dataclass(frozen=True)
class BoundingBox:
    """Polygon with list of bounding lat lon coords."""
    type: str
    coordinates: List[Position]


@dataclass(frozen=True)
class Geography(Node, IDNameLayer):
    """Represent a Geography reference record returned by the API."""
    bounding_box: Optional[BoundingBox]
    centre_point: Optional[Position]
    exclusion_rule: List[IDNameLayer]
    hierarchy: List[IDLayer]
    location: Position


@dataclass(frozen=True)
class GeographyEntity(EntityWithProbability):
    """

    Represents a hierarchy tree of locational data.

    [Geography Entities Further Documentation](https://docs.vortexa.com/reference/intro-geography-entries)


    """
