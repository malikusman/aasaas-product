import csv

def read_csv(file_path):
    """
    Reads a CSV file and returns a list of dictionaries containing the data.
    """
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return data
