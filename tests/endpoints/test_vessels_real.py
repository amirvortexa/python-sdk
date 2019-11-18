from unittest import TestCase, skipIf

from tests.config import SKIP_TAGS
from vortexasdk.client import create_client, set_client
from vortexasdk.endpoints.vessels import Vessels


@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
class TestVesselsReal(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        set_client(create_client())

    def test_search_ids(self):
        ids = [
            "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
            "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e"
        ]

        vessels = Vessels().search(ids=ids).to_list()
        assert len(vessels) == 2

        print([x.name for x in vessels])

    def test_search_filters_vessel_class(self):
        vessel_classes = [
            "vlcc_plus",
            "aframax"
        ]

        vessels = Vessels().search(vessel_classes=vessel_classes).to_list()

        actual = {x.vessel_class for x in vessels}

        assert actual == set(vessel_classes)

    def test_search_ids_dataframe(self):
        ids = [
            "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
            "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e"
        ]

        df = Vessels().search(ids=ids).to_df()
        assert list(df.columns) == ['id', 'name', 'imo', 'vessel_class']
        assert len(df) == 2
