import json
import csv

def write_to_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"✅ JSON data saved to: {output_path}")

def write_to_csv(data, output_path):
    fields = [
        "fr24_id", "flight", "callsign", "lat", "lon", "track", "alt",
        "gspeed", "vspeed", "squawk", "timestamp", "source", "hex", "type",
        "reg", "painted_as", "operating_as", "orig_iata", "orig_icao",
        "dest_iata", "dest_icao", "eta"
    ]

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

        for record in data:  # Each record = list of flights for one timestamp
            for flight in record:
                row = [flight.get(field, '') for field in fields]
                writer.writerow(row)

    print(f"✅ CSV data saved to: {output_path}")