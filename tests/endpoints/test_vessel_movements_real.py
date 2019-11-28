from datetime import datetime

from tests.testcases import TestCaseUsingRealAPI
from vortexasdk import VesselMovements
from vortexasdk.endpoints import vessel_movements_result


class TestVesselMovementsReal(TestCaseUsingRealAPI):
    def test_search(self):
        v = VesselMovements().search(
            filter_time_min=datetime(2017, 10, 1, 0, 0),
            filter_time_max=datetime(2017, 10, 1, 0, 10),
            filter_origins="rotterdam",
        )

        assert len(v) > 10

    def test_search_to_dataframe(self):
        df = (
            VesselMovements()
            .search(
                filter_time_min=datetime(2017, 10, 1, 0, 0),
                filter_time_max=datetime(2017, 10, 1, 0, 10),
                filter_origins="rotterdam",
            )
            .to_df()
            .head(2)
        )

        assert list(df.columns) == vessel_movements_result.DEFAULT_COLUMNS
        assert len(df) == 2

    def test_search_to_dataframe_subset_of_columns(self):
        cols = ["vessel.imo", "vessel.name"]
        df = (
            VesselMovements()
            .search(
                filter_time_min=datetime(2017, 10, 1, 0, 0),
                filter_time_max=datetime(2017, 10, 1, 0, 10),
                filter_origins="rotterdam",
            )
            .to_df(columns=cols)
            .head(2)
        )

        assert list(df.columns) == cols
        assert len(df) == 2
