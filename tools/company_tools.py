from langchain.tools import tool
from services.client_service import load_client_data, recommend_services

@tool
def find_similar_companies(company_name: str) -> str:
    """
    Mock function to find similar companies based on a company name.
    """
    mock_data = {
        "XYZ Corp": "ABC Inc, DEF Ltd",
        "Acme Corp": "GHI LLC, JKL PLC",
    }
    similar_companies = mock_data.get(company_name, "No similar companies found.")
    return f"Similar companies to {company_name}: {similar_companies}"

@tool
def recommend_client_services(client_name: str) -> str:
    """
    Recommend services for a client based on loaded data.
    """
    data = load_client_data("data/mock_clients.csv")
    return recommend_services(client_name, data)
