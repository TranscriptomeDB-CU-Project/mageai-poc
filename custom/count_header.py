from biostudies.utils.load_step.header import count_header

if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

@custom
def transform_custom(*args, **kwargs):
    count_header("/home/src/data/sdrf_cleaned_depth", "/home/src/data/count_header.txt")
