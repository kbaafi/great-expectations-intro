import pandas as pd


DATA_SOURCE = "../data/yellow_tripdata_2023-01.parquet"


def trips_sample_n(n=10000):
    trips_df = pd.read_parquet(DATA_SOURCE)
    trips_df = trips_df.sample(n)
    return trips_df

def trips_top_n(n=10000):
    trips_df = pd.read_parquet(DATA_SOURCE)
    trips_df = trips_df.head(n)
    return trips_df