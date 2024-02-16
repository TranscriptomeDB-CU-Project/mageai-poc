from biostudies.utils.in_depth_cleaning.column_groupper import ColumnGroupper
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
    groupper = ColumnGroupper("/home/src/data/embedding/cache")
    groupper.group("/home/src/sdrf_cleaned", "/home/src/column_group_file.txt")
