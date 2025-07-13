import json
import time
import os
import re
from datetime import datetime, timezone
from pathlib import Path
import json
from export import append_to_csv, append_to_json
from collect import collect_flight_data
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
    sleep_interval=SLEEP_SECONDS,
    write_csv=WRITE_CSV,
    write_json=WRITE_JSON,
    csv_path=CSV_PATH,
    json_path=JSON_PATH
)
# ================== Export ==================

if WRITE_JSON:
    append_to_json(flight_data, JSON_PATH)

if WRITE_CSV:
    append_to_csv(flight_data, CSV_PATH)

print("✅Data collection and export complete.")





