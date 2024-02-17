import os
os.chdir("/home/src/biostudies/utils/in_depth_cleaning")
from biostudies.utils.in_depth_cleaning.in_depth_cleaning import InDepthCleaning
os.chdir("/home/src")

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here
    cleaner = InDepthCleaning("/home/src/data/embedding/cache", "/home/src/data/column_group_file.txt")

    if not os.path.exists("/home/src/data/sdrf_cleaned_depth"):
        os.mkdir("/home/src/data/sdrf_cleaned_depth")

    cleaner.clean_all("/home/src/data/sdrf_cleaned", "/home/src/data/sdrf_cleaned_depth")