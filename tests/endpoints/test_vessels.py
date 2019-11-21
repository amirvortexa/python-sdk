from unittest import TestCase

from tests.mixins import CallMockAPI
from vortexasdk.endpoints.vessels import Vessels


class TestVessels(CallMockAPI, TestCase):

    def test_search_ids_retreives_names(self):
        vessels = Vessels().search().to_list()

        names = [x.name for x in vessels]

        assert names == ['0', '058']
