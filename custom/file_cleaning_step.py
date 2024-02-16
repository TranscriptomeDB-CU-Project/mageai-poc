from biostudies.utils.helper.file_cleaning import file_cleaning
import os

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

    column_name = read_column_mapping("/home/src/data/column_name_cleaned.txt")
    file_list = os.listdir("/home/src/data/sdrf")

    if not os.path.exists("/home/src/data/sdrf_cleaned"):
        os.mkdir("/home/src/data/sdrf_cleaned")

    for file in file_list:
        accession = file.split(".")[0]
        file_cleaning(accession, f"/home/src/data/sdrf/{file}", f"/home/src/data/sdrf_cleaned/{file}", column_name)
