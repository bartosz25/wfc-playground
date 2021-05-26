import shutil

from pyspark import Row
from pyspark.sql import SparkSession, functions

Player = Row("player_id", "goals", "assists")

spark = SparkSession.builder.master("local[*]")\
    .appName("Generate test files {}".format(__file__)).getOrCreate()
players = spark.createDataFrame([
    Player(100, 1, 2), Player(200, 3, 4), Player(300, 5, 6),
    Player(400, 7, 8)
])

output_dir = "/tmp/feast"
writer = players.withColumn("event_time", functions.current_timestamp()).coalesce(1).write
writer.format("parquet").mode("overwrite").save(output_dir)

import os
for parquet_candidate in os.listdir(output_dir):
    if parquet_candidate.endswith("parquet"):
        print(f'Renaming {parquet_candidate}')
        shutil.copy(f'{output_dir}/{parquet_candidate}', '/home/bartosz/workspace/wfc-playground/feature-store-feast/input/players.parquet')
        #os.rename(f'{output_dir}/{parquet_candidate}', f'{output_dir}/players.parquet')
