"""Time Series Endpoint."""
from datetime import datetime
from typing import List, Union

from vortexasdk.api.shared_types import to_ISODate
from vortexasdk.endpoints.endpoints import CARGO_TIMESERIES_RESOURCE
from vortexasdk.endpoints.timeseries_result import TimeSeriesResult
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list


class CargoTimeSeries(Search):
    _MAX_PAGE_RESULT_SIZE = 500

    def __init__(self):
        Search.__init__(self, CARGO_TIMESERIES_RESOURCE)

    def search(
        self,
        filter_activity: str,
        timeseries_frequency: str = "day",
        timeseries_unit: str = "b",
        filter_time_min: datetime = datetime(2019, 10, 1, 0),
        filter_time_max: datetime = datetime(2019, 10, 1, 1),
        filter_charterers: Union[str, List[str]] = None,
        filter_destinations: Union[str, List[str]] = None,
        filter_origins: Union[str, List[str]] = None,
        filter_owners: Union[str, List[str]] = None,
        filter_products: Union[str, List[str]] = None,
        filter_vessels: Union[str, List[str]] = None,
        filter_storage_locations: Union[str, List[str]] = None,
        filter_ship_to_ship_locations: Union[str, List[str]] = None,
        filter_waypoints: Union[str, List[str]] = None,
        disable_geographic_exclusion_rules: bool = None,
    ) -> TimeSeriesResult:
        """

        Find Aggregate flows between regions, for various products, for various vessels, or various corporations.

        Example questions that can be answered with this endpoint:

        * _How many Crude/Condensate barrels have been imported into China each day over the last year?_
        * _How many tonnes of Fuel Oil has company X exported from the United States each week over the last 2 years?_

        # Arguments
            filter_activity: Movement activity on which to base the time filter. Must be one of ['loading_state',
             'loading_start', 'loading_end', 'identified_for_loading_state', 'unloading_state', 'unloading_start',
              'unloading_end', 'storing_state', 'storing_start', 'storing_end', 'transiting_state'].

            timeseries_frequency: Frequency denoting the granularity of the time series. Must be one of ['day', 'week',
             'doe_week', 'month', 'quarter', 'year']

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            timeseries_unit: A numeric metric to be calculated for each time bucket. Must be one of ['b', 'bpd', 't',
             'tpd', 'c', 'cpd'], corresponding to barrels, barrels per day, metric tonnes, metric tonnes per day,
              cargo movement count, cargo movement count per day, respectively.

            filter_time_min: The UTC start date of the time filter.

            filter_time_max: The UTC end date of the time filter.

            cm_unit: Unit of measurement. Enter 'b' for barrels or 't' for tonnes.

            filter_corporations: A corporation ID, or list of corporation IDs to filter on.

            filter_destinations: A geography ID, or list of geography IDs to filter on.

            filter_origins: A geography ID, or list of geography IDs to filter on.

            filter_owners: An owner ID, or list of owner IDs to filter on.

            filter_products: A product ID, or list of product IDs to filter on.

            filter_vessels: A vessel ID, or list of vessel IDs to filter on.

            filter_storage_locations: A geography ID, or list of geography IDs to filter on.

            filter_ship_to_ship_locations: A geography ID, or list of geography IDs to filter on.

            filter_waypoints: A geography ID, or list of geography IDs to filter on.

            disable_geographic_exclusion_rules: This controls a popular industry term "intra-movements" and determines
             the filter behaviour for cargo leaving then entering the same geographic area.

        # Returns
        `TimeSeriesResult`

        # Example

        * _What was the monthly average barrels per day of crude loaded from Rotterdam over the last year?_

        ```python
        >>> from vortexasdk import CargoTimeSeries, Geographies, Products
        >>> rotterdam = [g.id for g in Geographies().search("rotterdam").to_list() if "port" in g.layer]
        >>> crude = [p.id for p in Products().search("crude").to_list() if "Crude" == p.name]
        >>> search_result = CargoTimeSeries().search(
        ...    timeseries_unit='bpd',
        ...    timeseries_frequency='month',
        ...    filter_origins=rotterdam,
        ...    filter_products=crude,
        ...    filter_activity='loading_state',
        ...    filter_time_min=datetime(2018, 1, 1),
        ...    filter_time_max=datetime(2018, 12, 31))
        >>> df = search_result.to_df()

        ```

        Gives the following:

        |    | key                      |     count |     value |
        |---:|:-------------------------|----------:|----------:|
        |  0 | 2018-01-01T00:00:00.000Z | 0.354839  | 458665    |
        |  1 | 2018-02-01T00:00:00.000Z | 0.75      | 45024     |
        |  2 | 2018-03-01T00:00:00.000Z | 0.0645161 |  35663.5  |
        |  3 | 2018-04-01T00:00:00.000Z | 0.878777  |  12345.2  |
        |  4 | 2018-05-01T00:00:00.000Z | 0.455932  |   9999.32 |
        |  5 | 2018-06-01T00:00:00.000Z | 0.777667  |  12234.8  |
        |  6 | 2018-07-01T00:00:00.000Z | 0.555097  | 987666    |
        |  7 | 2018-08-01T00:00:00.000Z | 0.290323  | 5318008.1 |
        |  8 | 2018-09-01T00:00:00.000Z | 0.0333333 | 686888.87 |
        |  9 | 2018-10-01T00:00:00.000Z | 0.354839  | 234344    |
        | 10 | 2018-11-01T00:00:00.000Z | 0.2345    | 111111    |
        | 11 | 2018-12-01T00:00:00.000Z | 0.123129  |  34344.5  |


        """
        params = {
            "timeseries_frequency": timeseries_frequency,
            "timeseries_unit": timeseries_unit,
            "timeseries_activity": filter_activity,
            "filter_activity": filter_activity,
            "filter_time_min": to_ISODate(filter_time_min),
            "filter_time_max": to_ISODate(filter_time_max),
            "size": self._MAX_PAGE_RESULT_SIZE,
            "filter_charterers": convert_to_list(filter_charterers),
            "filter_owners": convert_to_list(filter_owners),
            "filter_products": convert_to_list(filter_products),
            "filter_vessels": convert_to_list(filter_vessels),
            "filter_destinations": convert_to_list(filter_destinations),
            "filter_origins": convert_to_list(filter_origins),
            "filter_storage_locations": convert_to_list(
                filter_storage_locations
            ),
            "filter_ship_to_ship_locations": convert_to_list(
                filter_ship_to_ship_locations
            ),
            "filter_waypoints": convert_to_list(filter_waypoints),
            "disable_geographic_exclusion_rules": disable_geographic_exclusion_rules,
        }

        return TimeSeriesResult(super().search(**params))