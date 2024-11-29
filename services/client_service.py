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
    Recommend services for a specific client and suggest related services.
    """
    for client in data:
        if client['Name'].lower() == client_name.lower():
            related_services = categorize_services(client['Services Taken'])
            return (
                f"Services recommended for {client_name}: {client['Services Taken']}.\n"
                f"Reason: {client['Why with Us']}.\n"
                f"Related Services: {', '.join(related_services)}"
            )
    return f"No recommendations found for {client_name}."


def categorize_services(service: str) -> list:
    """
    Recommend related services based on the service taken.
    """
    service_map = {
        "Cloud Optimization": ["Cost Optimization", "Resource Monitoring"],
        "Data Analytics": ["Business Insights", "AI-Powered Dashboards"],
        "IT Infrastructure": ["Network Security", "Cloud Backup"],
        "Cloud Migration": ["Disaster Recovery", "Performance Tuning"],
    }
    return service_map.get(service, [])

