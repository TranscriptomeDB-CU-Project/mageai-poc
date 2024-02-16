import io
import os
import requests
import subprocess
# from dotenv import load_dotenv

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def load_data_from_api(**kwargs) -> None:
    """
    Template for loading data from API
    """

    MONGO_URI = kwargs['MONGO_URI']
    subprocess.run(["/home/src/biostudies/main /home/src/data"], 
        shell=True,
        check=True,
        env={
            "MONGO_URI": MONGO_URI
        }
    )
