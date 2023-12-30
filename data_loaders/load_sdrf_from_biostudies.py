import io
import os
import pandas as pd
import requests
import subprocess
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def load_data_from_api(**kwargs) -> DataFrame:
    """
    Template for loading data from API
    """

    MONGO_URI = kwargs['configuration'].get('MONGO_URI')

    subprocess.run(["./biostudies/utils/main /home/src/biostudies/data"], shell=True, check=True, env={
        "MONGO_URI": MONGO_URI
    })
