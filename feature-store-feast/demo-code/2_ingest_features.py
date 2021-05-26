from feast import Client

client = Client(
    core_url="localhost:6565",
    serving_url="localhost:6566"
)

client.ingest('players',
              source='file:///home/bartosz/workspace/wfc-playground/feature-store-feast/input/players.parquet')
