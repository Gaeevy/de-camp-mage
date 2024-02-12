import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date

    rename_dict = {
            'VendorID': 'vendor_id',
            'RatecodeID': 'ratecode_id',
            'PULocationID': 'pu_location_id',
            'DOLocationID': 'do_location_id',
        }
    data = data.rename(columns=rename_dict)

    return data


@test
def test_output(df, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, "df can't be None"
