import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url_pattern = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{month}.parquet"

    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'store_and_fwd_flag': pd.CategoricalDtype(['N', 'Y']),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    dfs = []
    for month in range(1, 13):
        month = '0' + str(month)
        url = url_pattern.format(month=f"2022-{month[-2:]}")
        df = pd.read_parquet(
                url,
            )
        df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
        df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"])
        dfs.append(df)
    df = pd.concat(dfs)

    return df
    


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
