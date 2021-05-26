import feast_spark
import pandas as pd
from feast import Client

client = Client(
    core_url="localhost:6565",
    serving_url="localhost:6566",
    spark_staging_location="file:///home/bartosz/workspace/wfc-playground/feature-store-feast/staging",
    spark_launcher="standalone",
    # The version we're using here for the
    spark_home="/home/bartosz/learning/apache_spark/envs/spark-3.0.2-bin-hadoop3.2"
)

player = pd.DataFrame(columns=['player_id', 'event_timestamp'])
player['player_id'] = [100, 200, 300, 400, 500, 600]
player['event_timestamp'] = pd.to_datetime(
    ['2021-05-25T00:00:00.000']*6)
# it's for lower or equal to // dataset created at 24/05 during the day;
# if you set 24 => it returns null, if you set 25, it finds rows!

historical_feature_retrieval_job = feast_spark.Client(client).get_historical_features(
    feature_refs=['players:assists', 'players:goals'],
    entity_source=player,
    output_location='file:///home/bartosz/workspace/wfc-playground/feature-store-feast/output_features'
)
