import os
import pandas as pd
import json

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'IIP_2021IcebergSeason.csv')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', '2021Icebergs.json')


def convert_csv_to_json():
    try:
        data = pd.read_csv(DATA_PATH)
        json_data = []

        print(f"Total Rows in CSV: {len(data)}")

        for index, row in data.iterrows():
            try:
                entry = {
                    "ID": f"ICE-{row['ICEBERG_NUMBER']}",
                    "Timestamp": f"{row['SIGHTING_DATE']} {str(row['SIGHTING_TIME']).zfill(4)}",
                    "Latitude": row['SIGHTING_LATITUDE'],
                    "Longitude": row['SIGHTING_LONGITUDE'],
                    "SightingMethod": row['SIGHTING_METHOD'],
                    "Size": row['SIZE'],
                    "Shape": row['SHAPE'],
                    "Source": row['SOURCE']
                }
                json_data.append(entry)

            except KeyError as e:
                print(f"Skipping row {index}: Missing column - {e}")
            except Exception as e:
                print(f"Error processing row {index}: {e}")

        print(f"Total Entries Processed: {len(json_data)}")

        with open(OUTPUT_PATH, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"JSON file created at: {OUTPUT_PATH}")

    except FileNotFoundError:
        print(f"File not found: {DATA_PATH}")
    except Exception as e:
        print(f"Error during conversion: {e}")