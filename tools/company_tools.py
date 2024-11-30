from database import SessionLocal, Company, Client
from langchain.tools import tool
from services.client_service import load_client_data, recommend_services
from config import CLIENT_CSV_MAPPING

@tool
def find_similar_companies(client_name: str, current_clients: list = None) -> str:
    """
    Find similar companies based on the client's existing clients.
    This function retrieves the current clients of the company and suggests similar companies
    based on a predefined mock dataset.
    """
    db = SessionLocal()
    try:
        # Fetch all companies associated with the given client name
        company_ids = db.query(Client.company_id).filter(Client.name == client_name).distinct().all()
        
        if not company_ids:
            return f"No parent company found for the client '{client_name}'."

        # Since there may be multiple companies, fetch the first one for now (can extend logic later)
        company_id = company_ids[0][0]  # Extract the first company_id from the query result
        company = db.query(Company).filter(Company.id == company_id).first()

        if not company:
            return f"No company details found for ID {company_id}."

        # Fetch all clients under this company
        clients = db.query(Client).filter_by(company_id=company.id).all()
        current_clients = [client.name for client in clients]

        if not current_clients:
            return f"No clients found for the company '{company.name}'."

        print(f"Clients of {company.name}: {current_clients}")

        # Mock implementation for now
        mock_data = {
            "Du": "Etisalat, STC",
            "Damac": "Emaar, Nakheel",
            "XYZ Corp": "ABC Corp, DEF Corp"
        }
        # Use the first client for mock logic
        return mock_data.get(client_name, "No similar companies found.")
    finally:
        db.close()

@tool
def recommend_client_services(client_name: str) -> str:
    """
    Dynamically recommend services for a client based on their CSV.
    """
    csv_file = CLIENT_CSV_MAPPING.get(client_name, "data/default_clients.csv")
    data = load_client_data(csv_file)
    return recommend_services(client_name, data)
