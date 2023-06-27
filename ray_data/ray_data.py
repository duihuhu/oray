import ray
ray.init()
ds = ray.data.read_parquet([
    "s3://anonymous@air-example-data/ursa-labs-taxi-data/downsampled_2009_01_data.parquet",
    "s3://anonymous@air-example-data/ursa-labs-taxi-data/downsampled_2009_02_data.parquet"
])
ds.schema()
ds.count()
ds.max(["trip_distance", "tip_amount", "passenger_count"])
ds.groupby("passenger_count").count().take()

