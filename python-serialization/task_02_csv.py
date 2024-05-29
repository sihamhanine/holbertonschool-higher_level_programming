#!/usr/bin/python3
import json
import csv


def convert_csv_to_json(csv_filename):
    """
    Method that convert the csv data to a json file
    and writes it to data.json.

    Args:
        csv_filename: the csv filename to read from
    Returns:
        bool: True if the conversion was successful,
        False otherwise.
    """
    try:
        with open(csv_filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = []
            for row in reader:
                data.append(row)
        with open('data.json', "w") as jsonfile:
            json.dump(data, jsonfile)
        return True
    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
