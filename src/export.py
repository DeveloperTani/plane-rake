import json
import csv

def write_to_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"✅ JSON data saved to: {output_path}")

def write_to_csv(data, output_path):
    fields = [
        "timestamp", "iso_time", "fr24_id", "flight", "callsign", "lat", "lon", "track", "alt",
        "gspeed", "vspeed", "squawk", "source", "hex", "type",
        "reg", "painted_as", "operating_as", "orig_iata", "orig_icao",
        "dest_iata", "dest_icao", "eta"
    ]

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

        for record in data:
            timestamp = record.get("timestamp")
            iso_time = record.get("iso_time")
            flights = record.get("flights", [])

            if not flights:
                writer.writerow([timestamp, iso_time] + [""] * (len(fields) - 2))
            else:
                for flight in flights:
                    row = [timestamp, iso_time] + [flight.get(field, '') for field in fields[2:]]
                    writer.writerow(row)

    print(f"✅ CSV data saved to: {output_path}")