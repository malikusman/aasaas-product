import csv

def load_client_data(file_path: str):
    """
    Load client data from a CSV file.
    """
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
