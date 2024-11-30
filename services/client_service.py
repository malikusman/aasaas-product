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

def generate_llm_prompt(client_name: str, current_clients: list) -> str:
    """
    Generate a detailed prompt for the LLM based on client context.
    """
    clients_str = ", ".join(current_clients)
    return (
        f"Client {client_name} provides services to these companies: {clients_str}. "
        f"Please find companies similar to these and suggest what services {client_name} can offer them. "
        f"Provide detailed and actionable recommendations."
    )


