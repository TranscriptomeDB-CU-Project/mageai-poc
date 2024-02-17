import os
from biostudies.utils.basic_cleaning.extract_header import extract_header

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

@custom
def transform_custom(*args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        df (DataFrame): Data frame from parent block.

    Returns:
        DataFrame: Transformed data frame
    """
    extract_header(sdrf_path="/home/src/data/sdrf", column_name_path="/home/src/data/column_name.txt", attribute_path="/home/src/data/attribute.txt")

