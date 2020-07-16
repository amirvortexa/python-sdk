import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from vortexasdk.api import Product
from vortexasdk.api.entity_flattening import flatten_dictionary
from vortexasdk.api.search_result import Result
from vortexasdk.create_dataframe import create_dataframe
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class ProductResult(Result):
    """Container class that holds the result obtained from calling the `Product` endpoint."""

    def to_list(self) -> List[Product]:
        """Represent products as a list."""
        list_of_dicts = super().to_list()

        with Pool(os.cpu_count()) as pool:
            logger.debug(
                f"Converting dictionary to Products using {os.cpu_count()} processes"
            )
            return list(pool.map(Product.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent products as a `pd.DataFrame`.

        # Arguments
            columns: The product features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'layer.0', 'parent.0.name']`.


        # Returns
        `pd.DataFrame` of products.

        """
        flattened_dicts = [flatten_dictionary(p) for p in super().to_list()]

        return create_dataframe(
            columns=columns,
            default_columns=DEFAULT_COLUMNS,
            data=flattened_dicts,
            logger_description="Products",
        )


DEFAULT_COLUMNS = ["id", "name", "layer.0", "parent.0.name"]
