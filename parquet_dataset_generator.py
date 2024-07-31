import pandas as pd
import json
import glob


def combine_json_arrays(directory_path: str) -> list:
    combined_array = []
    json_files = glob.glob(directory_path + "/*.json")

    for file_name in json_files:
        with open(file_name, 'r') as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    combined_array.extend(data)
                else:
                    print(f"Warning: {file_name} does not contain a JSON array.")
            except Exception as e:
                print(f"Error decoding JSON from file {file_name}: {e}")

    return combined_array


def create_parquet_from_json(json_data: list):
    dataset_raw_combined = {"conversations": json_data}
    df = pd.DataFrame(dataset_raw_combined)
    df.to_parquet('internal_dataset.parquet', index=False)


if __name__ == "__main__":
    raw_json_data = combine_json_arrays(".")
    create_parquet_from_json(raw_json_data)
