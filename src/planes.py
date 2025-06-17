import json
import time
import os
import re
from datetime import datetime, timezone
from pathlib import Path

from collect import collect_flight_data
from export import write_to_json, write_to_csv
from config import *

# ================== Preprocessing ==================

# Format timestamp for filename
timestamp_label = datetime.strptime(START_TIME_STRING, "%Y-%m-%d %H:%M").strftime("%Y%m%dT%H%M")

# Clean bounds (remove spaces and commas)
bounds_clean = re.sub(r'[^\d.-]', '', BOUNDS.replace(',', '_'))

# Create base filename
base_filename = f"flightdata_{timestamp_label}_{bounds_clean}"

# Paths
BASE_DIR = Path(__file__).resolve().parent
JSON_PATH = BASE_DIR / f"data/JSON/{base_filename}.json"
CSV_PATH = BASE_DIR / f"data/CSV/{base_filename}.csv"

# Ensure output directories exist
os.makedirs(JSON_PATH.parent, exist_ok=True)
os.makedirs(CSV_PATH.parent, exist_ok=True)

# Timestamps
START_TIMESTAMP = int(datetime.strptime(START_TIME_STRING, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc).timestamp())
END_TIMESTAMP = START_TIMESTAMP + DURATION_SECONDS

# ================== Data Collection ==================

flight_data = collect_flight_data(
    start_ts=START_TIMESTAMP,
    end_ts=END_TIMESTAMP,
    bounds=BOUNDS,
    token=TOKEN,
    log_interval=LOG_RATE_SECONDS,
    sleep_interval=SLEEP_SECONDS
)

# ================== Export ==================

if WRITE_JSON:
    write_to_json(flight_data, JSON_PATH)

if WRITE_CSV:
    write_to_csv(flight_data, CSV_PATH)

print("✅Data collection and export complete.")






# # Open a file to write the data
# with open(FILE_PATH, 'w') as outfile:
#     # Write an opening square bracket for a JSON array
#     outfile.write('[\n')

#     first_entry = True  # Flag to manage comma placement in JSON file

#     # Loop through the hour with 30-second intervals
#     for timestamp in range(START_TIMESTAMP, END_TIMESTAMP, LOG_RATE_SECONDS):  # Loop from start to end timestamp with user-specified intervals
#         params = {
#             'bounds': bounds,
#             'timestamp': timestamp
#         }

#         print(f"\nQuerying data for timestamp: {datetime.fromtimestamp(timestamp, tz=timezone.utc)}")
#         print(timestamp)


#         try:
#             response = requests.get(url, headers=headers, params=params)
#             response.raise_for_status()
#             data = response.json()


#             # Check if 'data' exists and is not an empty list
#             if isinstance(data, dict) and 'data' in data:
#                 flight_data = data['data']
#                 print(f"[{datetime.fromtimestamp(timestamp, tz=timezone.utc)}] Flights found: {len(flight_data)}")

#                 # Write the JSON data into the file
#                 if len(flight_data) > 0:
                        
#                     if not first_entry:
#                         outfile.write(',\n')
#                     else:
#                         first_entry = False

#                     json.dump(flight_data, outfile, indent=4)
#             else:
#                 print(f"[{datetime.fromtimestamp(timestamp, tz=timezone.utc)}] No flight data found.")

#         except requests.exceptions.HTTPError as http_err:
#             print(f"HTTP error occurred: {http_err}")
#         except Exception as err:
#             print(f"An error occurred: {err}")

#         # Sleep to stay under the API rate limit (e.g. 10 req/min for Explorer plan)
#         time.sleep(SLEEP_SECONDS)

#     outfile.write('\n]')

# print(f"Data collection completed and saved to '{FILE_PATH}'.")


