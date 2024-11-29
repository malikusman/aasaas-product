import csv

def load_client_data(file_path: str):
    """
    Load client data from a CSV file.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def recommend_services(client_name: str, data: list):
    """
    Recommend services for a specific client.
    """
    for client in data:
        if client['Name'].lower() == client_name.lower():
            return f"Services recommended for {client_name}: {client['Services Taken']}. Reason: {client['Why with Us']}."
    return f"No recommendations found for {client_name}."
