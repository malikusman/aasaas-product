from langchain.tools import tool

@tool
def find_similar_companies(company_name: str) -> str:
    """
    Mock function to find similar companies based on a company name.
    Replace this with real logic in the future (e.g., web scraping or querying APIs).
    """
    mock_data = {
        "XYZ Corp": "ABC Inc, DEF Ltd",
        "Acme Corp": "GHI LLC, JKL PLC",
    }
    similar_companies = mock_data.get(company_name, "No similar companies found.")
    return f"Similar companies to {company_name}: {similar_companies}"
