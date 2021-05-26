import datetime
import time

import feast_spark
from feast import Client
from feast.core.IngestionJob_pb2 import COMPLETED, ERROR

client = Client(
    core_url="localhost:6565",
    serving_url="localhost:6566",
    spark_staging_location="file:///home/bartosz/workspace/wfc-playground/feature-store-feast/staging",
    spark_launcher="standalone",
    # The version we're using here for the
    spark_home="/home/bartosz/learning/apache_spark/envs/spark-3.0.2-bin-hadoop3.2"
)

players_feature_table = client.get_feature_table('players')
job = feast_spark.Client(client).start_offline_to_online_ingestion(players_feature_table,
                                                                   start=datetime.datetime(2021, 1, 1),
                                                                   end=datetime.datetime(2021, 5, 31))

# Not very smart way to deal with async jobs
# but surprisingly, even client.list_jobs(include_terminated=True) always
# returns an empty array and I didn't find a way to wait in a smarter way
time.sleep(50)
