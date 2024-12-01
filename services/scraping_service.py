import requests
from bs4 import BeautifulSoup

def scrape_similar_companies(company_name):
    """
    Scrape Google search results to find similar companies to the given company name.
    :param company_name: Name of the company to search for similar companies.
    :return: List of similar companies (mocked for simplicity).
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    query = f"companies similar to {company_name}"
    url = f"https://www.google.com/search?q={query}"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to fetch data for {company_name}"

    soup = BeautifulSoup(response.text, "html.parser")
    # Example: Extract search result titles (customize based on actual page structure)
    search_results = soup.find_all("h3", limit=5)  # Get the first 5 search results
    similar_companies = [result.text for result in search_results]

    # Mock results if scraping fails
    if not similar_companies:
        similar_companies = ["Mock Company A", "Mock Company B", "Mock Company C"]

    return similar_companies
