import os
import importlib

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

@custom
def transform(*args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    os.chdir("/home/src/data")

    from biostudies.utils.helper.age.extract_col.extract_col import run_extract_col
    from biostudies.utils.helper.age.extract_col.find_similar_col import find_similar_col
    
    run_extract_col()
    find_similar_col()
