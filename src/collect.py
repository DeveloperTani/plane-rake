import requests
import time
from datetime import datetime, timezone


def collect_flight_data(start_ts, end_ts, bounds, token, log_interval, sleep_interval):
    url = 'https://fr24api.flightradar24.com/api/historic/flight-positions/full'
    headers = {
        'Accept': 'application/json',
        'Accept-Version': 'v1',
        'Authorization': f'Bearer {token}'
    }

    all_flights = []

    for timestamp in range(start_ts, end_ts, log_interval):
        params = {
            'bounds': bounds,
            'timestamp': timestamp
        }

        ts_readable = datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()
        print(f"🔍 Querying: {ts_readable}")

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            if 'data' in data and data['data']:
                flight_data = data['data']
                print(f"✈️  Flights found: {len(flight_data)}")
                all_flights.append(flight_data)
            else:
                print("⚠️  No flight data found.")

        except requests.exceptions.HTTPError as http_err:
            print(f"❌ HTTP error: {http_err}")
        except Exception as err:
            print(f"❌ General error: {err}")

        time.sleep(sleep_interval)

    return all_flights