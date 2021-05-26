from feast import Feature, ValueType, Entity, FeatureTable, FileSource, Client
from feast.data_format import ParquetFormat

goals = Feature("goals", ValueType.INT64)
assists = Feature("assists", ValueType.INT64)
player_id_entity = Entity(name="player_id", description="Player unique ID", value_type=ValueType.INT64)
players_feature_table = FeatureTable(
    name="players",
    entities=["player_id"],
    features=[goals, assists],
    labels={
        "creation_time": "2021-05-24T08:00",
        "author": "waitingforcode"
    },
    batch_source=FileSource(
        file_format=ParquetFormat(),
        event_timestamp_column="event_time",
        created_timestamp_column="event_time",
        # It's the output destination for the batch_source!
        # Every time you call #ingest for this feature table,
        # Feast will write the ingested data to this location!
        file_url="file:///home/bartosz/workspace/wfc-playground/feature-store-feast/input"
    )
)

client = Client(
    core_url="localhost:6565",
    serving_url="localhost:6566"
)
# grpc.RpcError: Feature Table refers to no existent Entity: (table: driver_statistics, entity: driver_id, project: default)
# We have to call all previously defined entities!
client.apply(player_id_entity)
client.apply(players_feature_table)

# Check whether all features are there
features = client.list_features_by_ref(entities=[player_id_entity.name])
print(features)
