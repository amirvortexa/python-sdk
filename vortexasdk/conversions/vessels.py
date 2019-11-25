from typing import List, Union

from vortexasdk.api import ID
from vortexasdk.api.id import split_ids_other
from vortexasdk.conversions.conversions import _search_ids
from vortexasdk.endpoints.vessels import AVAILABLE_VESSEL_CLASSES, Vessels


def convert_to_vessel_ids(
    vessel_attributes: List[Union[ID, str, int]]
) -> List[ID]:
    """
    Convert a mixed list of names, IDs, IMOs, or MMSIs to vessel ids.

    # Example
    ```
        >>> convert_to_vessel_ids(["Stallion", 9464326, 477639900, 'vlcc'])
    ['e486ca3d2e58b61d683b5143a063ec309f2fa3bfd0b87d91984f43d9ee5071fb',...]
    ```
    """
    ids, others = split_ids_other(vessel_attributes)

    vessel_classes = []
    names_imos_mmsis = []
    for e in others:
        if e in AVAILABLE_VESSEL_CLASSES:
            vessel_classes.append(e)
        else:
            names_imos_mmsis.append(e)

    vessels_matched_on_vessel_class = (
        _search_ids(Vessels(), vessel_classes=vessel_classes)
        if len(vessel_classes) > 0
        else []
    )

    vessels_matched_on_name_imo_mmsi = (
        _search_ids(Vessels(), term=names_imos_mmsis)
        if len(names_imos_mmsis) > 0
        else []
    )

    return (
        ids
        + vessels_matched_on_vessel_class
        + vessels_matched_on_name_imo_mmsi
    )
