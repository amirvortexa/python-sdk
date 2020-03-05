from datetime import datetime

from docs.utils import to_markdown
from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import Geographies, Products
from vortexasdk.endpoints.cargo_timeseries import CargoTimeSeries


class TestCargoTimeSeries(TestCaseUsingRealAPI):
    def test_search_returns_one_day(self):
        date = datetime(2019, 11, 10)

        result = CargoTimeSeries().search(
            filter_activity="loading_state",
            filter_time_min=date,
            filter_time_max=date,
        )

        assert len(result) == 1

    def test_search_returns_all_days(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        result = CargoTimeSeries().search(
            filter_activity="loading_state",
            filter_time_min=start,
            filter_time_max=end,
        )

        n_days = (end - start).days + 1

        assert n_days == len(result)

    def test_to_df(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        df = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_df()
        )

        print(to_markdown(df.head()))

        n_days = (end - start).days + 1

        assert len(df) == n_days
        assert list(df.columns) == ["key", "value", "count"]

    def test_to_list(self):
        start = datetime(2019, 11, 1)
        end = datetime(2019, 11, 10)

        time_series_list = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                filter_time_min=start,
                filter_time_max=end,
            )
            .to_list()
        )

        n_days = (end - start).days + 1

        assert len(time_series_list) == n_days

    def test_filter_geographies_and_products(self):
        start = datetime(2019, 1, 1)
        end = datetime(2019, 11, 1)

        rotterdam = [
            g.id
            for g in Geographies().search(term="rotterdam").to_list()
            if "port" in g.layer
        ]
        crude = [
            p.id
            for p in Products().search("crude").to_list()
            if "Crude" == p.name
        ]

        rotterdam_crude_timeseries = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_unit="bpd",
                timeseries_frequency="month",
                filter_time_min=start,
                filter_time_max=end,
                filter_origins=rotterdam,
                filter_products=crude,
            )
            .to_df()
        )

        rotterdam_all_products_timeseries = (
            CargoTimeSeries()
            .search(
                filter_activity="loading_state",
                timeseries_unit="bpd",
                timeseries_frequency="month",
                filter_time_min=start,
                filter_time_max=end,
                filter_origins=rotterdam,
            )
            .to_df()
        )

        assert (
            rotterdam_all_products_timeseries["value"].sum()
            > rotterdam_crude_timeseries["value"].sum()
        )

        print(rotterdam_crude_timeseries.head())