# from python_sdk.vessels import Vessels
# import pandas as pd
# ids = [
#     "6d8a8f0863ca087204dd68e5fc3b6469a879829e6262856e34856aea3ca20509",
#     "bf2b55bd31c709aa4cba91a3cc4111191c88c83753cbd285674c22150e42003e"
# ]
#
# Vessels().search(ids=ids).to_list()
# vessels = Vessels().search(ids=ids).to_df()
#
#
# v = Vessels().search(vessel_classes=['vlcc'], term='ocean').to_df(columns=['name', 'imo', 'mmsi', 'related_names'])
#
# from tabulate import tabulate
# print(tabulate(v, headers='keys', tablefmt='pipe'))
