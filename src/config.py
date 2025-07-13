from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("FR24_TOKEN")

BOUNDS = '60.544,60.430,25.155,25.478'     # 'north, south, west, east'
START_TIME_STRING = '2025-06-10 15:00'     # UTC
DURATION_SECONDS = 3600*24*30           # Total range (e.g., 1hr = 3600)
LOG_RATE_SECONDS = 15                      # Sampling interval
SLEEP_SECONDS = 6                          # Real-time delay between requests

WRITE_CSV = True
WRITE_JSON = True

if TOKEN is None:
    raise ValueError("API token not found. Did you set FR24_TOKEN in your .env file?")
