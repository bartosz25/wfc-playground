from feast import Client

client = Client(
    core_url="localhost:6565",
    serving_url="localhost:6566"
)

online_response = client.get_online_features(
    feature_refs=['players:assists', 'players:goals'],
    entity_rows=[{"player_id": 100}]
)
print(online_response.to_dict())

online_response = client.get_online_features(
    feature_refs=['players:assists', 'players:goals'],
    entity_rows=[{"player_id": 600}]
)
print(online_response.to_dict())
