from typing import List, Union

from vortexasdk.endpoints.vessels import Vessels
from vortexasdk.api import ID
from vortexasdk.conversions.conversions import _convert_to_ids


def convert_to_vessel_ids(ids_or_names_list: List[Union[ID, str]]) -> List[ID]:
    """
    Convert a mixed list of names or IDs to vessel ids.

    # Example
    ```
        >>> convert_to_vessel_ids(["Stallion"])
    ['e486ca3d2e58b61d683b5143a063ec309f2fa3bfd0b87d91984f43d9ee5071fb',...]
    ```
    """
    return _convert_to_ids(ids_or_names_list, Vessels())
