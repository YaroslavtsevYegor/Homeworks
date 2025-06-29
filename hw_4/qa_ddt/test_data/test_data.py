import csv
import os

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH = get_path(filename="auth_endpoints.csv")


def get_auth_endpoints():
    with open(CSV_FILE_PATH, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for el in reader:
            yield el


auth_endpoints = get_auth_endpoints()
