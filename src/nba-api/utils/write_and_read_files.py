"""
Util functions used for writing and reading csv and json files

Functions:
    write_json_from_dict
    read_json
    write_csv_from_matrix
    read_matrix_from_csv

"""
import csv
import json


def write_json_from_dict(my_dict: dict, path: str, **kwargs) -> None:
    """Writes dictionary to json file"""
    # Serialize json
    json_object = json.dumps(my_dict, indent=4)

    # Write to file
    with open(path, "w", encoding="utf-8") as data_file:
        data_file.write(json_object, **kwargs)


def read_json(path: str, **kwargs) -> dict | list[dict]:
    """Read contents of a json file"""
    with open(path, "r", encoding="utf-8") as input_file:
        contents = json.load(input_file, **kwargs)
    return contents


def write_csv_from_matrix(matrix: list[list], path: str, **kwargs) -> None:
    """
    Write a csv file from a matrix, i.e. a list of list,
    such that each row of the matrix corresponds to a row in the csv file
    """
    with open(path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, **kwargs)
        for row in matrix:
            writer.writerow(row)


def read_matrix_from_csv(path: str, **kwargs) -> list[list]:
    """
    Read contents of a csv file as a matrix, i.e. a list of list,
    such that each row of the matrix corresponds to a row in the csv file
    """
    with open(path, newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, **kwargs)
        matrix = list(reader)
    return matrix
