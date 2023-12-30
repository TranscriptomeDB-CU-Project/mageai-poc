from biostudies.utils.helper.column_cleaning import column_cleaning
import os

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

@custom
def transform(data, *args, **kwargs):
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
    column_cleaning()
