"""

Here we find all vessel movements chartered by specific corporations stored in a excel sheet.

First we we ingest an Excel spreadsheet [(which can be viewed here)](https://github.com/VorTECHsa/python-sdk/tree/master/docs/examples/resources/my_charterers.xlsx)
containing a custom list of charterers. We then convert these charter names to IDs, and search the VesselMovements
endpoint to find all recent vessel movements charterered by these firms.

The below script returns:

|    | vessel.name   |   vessel.imo |   vessel.mmsi |   vessel.cubic_capacity |   vessel.dwt | vessel.vessel_class   | origin.location.port.label   | destination.location.port.label   |   destination.location.sts_zone.label | origin.start_timestamp   | destination.end_timestamp   | cargoes.0.product.group.label   | vessel.corporate_entities.charterer.label   |   vessel.corporate_entities.time_charterer.label | vessel.corporate_entities.commercial_owner.label   |
|---:|:--------------|-------------:|--------------:|------------------------:|-------------:|:----------------------|:-----------------------------|:----------------------------------|:--------------------------------------|:-------------------------|:----------------------------|:--------------------------------|:--------------------------------------------|-------------------------------------------------:|:---------------------------------------------------|
|  0 | OLKA G LUCK   |      9235469 |     248575000 |                   89803 |        50199 | handymax              | Amsterdam [NL]               | Tianjin [CN]                      |                                   nan | 2020-05-22T15:00:34+0000 | nan                         | Clean Petroleum Products        | KOLMAR                                      |                                              nan | BoatBr S Shipping                                 |
|  1 | ALEXTA YLOR   |      9245611 |     335608000 |                   89123 |        53000 | handymax              | Houston, TX [US]             | Veracruz [MX]                     |                                   nan | 2020-06-06T21:10:16+0000 | 2020-06-08T09:19:40+0000    | Clean Petroleum Products        | KOCH                                        |                                              nan | KOCH                                               |

(The above data has been anonymised in this example)
"""
from datetime import datetime, timedelta
from typing import List

import pandas as pd

from vortexasdk import Corporations, VesselMovements
from vortexasdk.api import ID


def convert_to_corporation_ids(corporation_name: str) -> List[ID]:
    """
    Returns a list of all corporation IDs with the name `corporation_name`.
    This function returns a list, instead of a single ID. This is because some charterers may share the same name.

    :param corporation_name: The name of the corporation we'd like to look up
    :return: A list of IDs of corporations with a matching name
    """

    # The search returns all corporations with similar names.
    # For example, searching ADN would return both ADNOC and ADNATCO
    corporations_with_encapsulating_names = Corporations().search(corporation_name).to_list()

    # In this case we're only interested in corporations with an exact name match.
    return [c.id for c in corporations_with_encapsulating_names if c.name.upper() == corporation_name.upper()]

    # We could have chosen to keep the other corporations (with similar, but not exact names) like so:
    # return [c.id for c in corporations_with_encapsulating_names]


if __name__ == "__main__":
    # Read our excel sheet of charterers into a dataframe
    charterers_df = pd.read_excel("./resources/my_charterers.xlsx")

    # Convert the charterer names into ids
    charterers_list_of_lists = charterers_df['charterers'].apply(convert_to_corporation_ids).to_list()
    charterers = [item for sublist in charterers_list_of_lists for item in sublist]

    # Query API
    df = VesselMovements().search(
        filter_charterers=charterers,
        filter_time_min=datetime.now() - timedelta(weeks=1),
        filter_time_max=datetime.now(),
    ).to_df()

    print(df)
