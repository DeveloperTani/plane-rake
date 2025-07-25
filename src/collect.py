import requests
import time
from datetime import datetime, timezone
from export import init_csv_file, append_to_csv, append_to_json 

def collect_flight_data(start_ts, end_ts, bounds, token, log_interval, sleep_interval,
                        write_csv=False, write_json=False,
                        csv_path=None, json_path=None):

    url = 'https://fr24api.flightradar24.com/api/historic/flight-positions/full'
    headers = {
        'Accept': 'application/json',
        'Accept-Version': 'v1',
        'Authorization': f'Bearer {token}'
    }

    fields = init_csv_file(csv_path) if write_csv and csv_path else None
    all_flights = []

    for timestamp in range(start_ts, end_ts, log_interval):
        params = {
            'bounds': bounds,
            'timestamp': timestamp
        }

        ts_readable = datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()
        print(f"Querying: {ts_readable}")

        record = {
            "timestamp": timestamp,
            "iso_time": ts_readable,
            "flights": []  
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            if 'data' in data and data['data']:
                flight_data = data['data']
                print(f"Flights found: {len(flight_data)}")
                record["flights"] = flight_data
            else:
                print("No flight data found.")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error: {http_err}")
        except Exception as err:
            print(f"General error: {err}")

        # Always append record regardless of error
        all_flights.append(record)

        # Write after each log if enabled
        if write_json and json_path:
            append_to_json(record, json_path)

        if write_csv and csv_path and fields:
            append_to_csv(record, csv_path, fields)

        time.sleep(sleep_interval)

    return all_flights