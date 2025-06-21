from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("FR24_TOKEN")

BOUNDS = '60.400, 60.200, 24.800, 25.200'  # 'north, south, west, east'
START_TIME_STRING = '2025-06-09 14:00'     # UTC
DURATION_SECONDS = 3600                    # Total range (e.g., 1hr = 3600)
LOG_RATE_SECONDS = 30                      # Sampling interval
SLEEP_SECONDS = 6                          # Real-time delay between requests

WRITE_CSV = True
WRITE_JSON = True

if TOKEN is None:
    raise ValueError("API token not found. Did you set FR24_TOKEN in your .env file?")
