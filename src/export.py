import json
import csv
import os

def init_csv_file(output_path):
    """Create CSV file and write headers."""
    fields = [
        "timestamp", "iso_time", "fr24_id", "flight", "callsign", "lat", "lon", "track", "alt",
        "gspeed", "vspeed", "squawk", "source", "hex", "type",
        "reg", "painted_as", "operating_as", "orig_iata", "orig_icao",
        "dest_iata", "dest_icao", "eta"
    ]
    write_header = not os.path.exists(output_path)

    with open(output_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(fields)

    return fields

def append_to_csv(record, output_path, fields):
    """Append a single timestamped log entry to CSV."""
    timestamp = record.get("timestamp")
    iso_time = record.get("iso_time")
    flights = record.get("flights", [])

    with open(output_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        if not flights:
            writer.writerow([timestamp, iso_time] + [""] * (len(fields) - 2))
        else:
            for flight in flights:
                row = [timestamp, iso_time] + [flight.get(field, '') for field in fields[2:]]
                writer.writerow(row)

def append_to_json(record, output_path):
    """Append JSON log entry per timestamp (optional)."""
    with open(output_path, 'a', encoding='utf-8') as f:
        json.dump(record, f, indent=4)
        f.write(',\n') 