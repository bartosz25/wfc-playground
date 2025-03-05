import pandas as pd

from ydata_profiling import ProfileReport

local_trip_data_file_name = './yellow_tripdata_2024-01.parquet'
# Download the file from https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet
import urllib.request
urllib.request.urlretrieve('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet',
                           local_trip_data_file_name)

yellow_tripdata = pd.read_parquet(local_trip_data_file_name)
profile = ProfileReport(yellow_tripdata, title="Profiling Report",
                        correlations=None,
                        samples={"head": 0, "tail": 0})
alerts = profile.get_description().alerts
print("=== Alerts ===")
for alert in alerts:
    print(f"Alert: {alert.alert_type} / {alert.alert_type_name} / {alert.column_name} / {type(alert)}")
    print(f'Alert content={alert.fmt()} // {str(alert)}')
    #print(f"Affected variables: {alert.message}")

"""
=== Alerts ===
Alert: AlertType.IMBALANCE / Imbalance / store_and_fwd_flag / <class 'ydata_profiling.model.alerts.ImbalanceAlert'>
Alert: AlertType.IMBALANCE / Imbalance / payment_type / <class 'ydata_profiling.model.alerts.ImbalanceAlert'>
Alert: AlertType.IMBALANCE / Imbalance / improvement_surcharge / <class 'ydata_profiling.model.alerts.ImbalanceAlert'>
Alert: AlertType.IMBALANCE / Imbalance / Airport_fee / <class 'ydata_profiling.model.alerts.ImbalanceAlert'>
Alert: AlertType.MISSING / Missing / passenger_count / <class 'ydata_profiling.model.alerts.MissingAlert'>
Alert: AlertType.MISSING / Missing / RatecodeID / <class 'ydata_profiling.model.alerts.MissingAlert'>
Alert: AlertType.MISSING / Missing / store_and_fwd_flag / <class 'ydata_profiling.model.alerts.MissingAlert'>
Alert: AlertType.MISSING / Missing / congestion_surcharge / <class 'ydata_profiling.model.alerts.MissingAlert'>
Alert: AlertType.MISSING / Missing / Airport_fee / <class 'ydata_profiling.model.alerts.MissingAlert'>
Alert: AlertType.SKEWED / Skewed / trip_distance / <class 'ydata_profiling.model.alerts.SkewedAlert'>
Alert: AlertType.ZEROS / Zeros / passenger_count / <class 'ydata_profiling.model.alerts.ZerosAlert'>
Alert: AlertType.ZEROS / Zeros / trip_distance / <class 'ydata_profiling.model.alerts.ZerosAlert'>
Alert: AlertType.ZEROS / Zeros / extra / <class 'ydata_profiling.model.alerts.ZerosAlert'>
Alert: AlertType.ZEROS / Zeros / mta_tax / <class 'ydata_profiling.model.alerts.ZerosAlert'>
Alert: AlertType.ZEROS / Zeros / tip_amount / <class 'ydata_profiling.model.alerts.ZerosAlert'>
Alert: AlertType.ZEROS / Zeros / tolls_amount / <class 'ydata_profiling.model.alerts.ZerosAlert'>
Alert: AlertType.ZEROS / Zeros / congestion_surcharge / <class 'ydata_profiling.model.alerts.ZerosAlert'>

"""