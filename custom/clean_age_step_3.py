import importlib
import os

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom


@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here

    os.chdir("/home/src/data")

    step_3 = importlib.import_module("biostudies.utils.helper.age.3_parse_col")

    step_3.run_parse_col()
