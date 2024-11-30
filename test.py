from crud import add_company, add_client
from agents.create_agent import create_agent

# Add a company
company_data = {
    "name": "VaporVM",
    "email": "info@vaporvm.com",
    "contact_person": "John Doe",
    "phone": "1234567890",
    "website": "www.vaporvm.com"
}
company = add_company(company_data)

# Add clients for VaporVM
client_data_1 = {
    "company_id": company.id,
    "name": "Du",
    "services_taken": "Cloud Management, Server Hosting",
    "why_with_us": "Trust and expertise",
    "website": "www.du.ae",
    "email": "info@du.ae",
    "phone": "9876543210"
}
add_client(client_data_1)

client_data_2 = {
    "company_id": company.id,
    "name": "Damac",
    "services_taken": "Cloud Management, Cloud Monitoring",
    "why_with_us": "Cost savings",
    "website": "www.damac.com",
    "email": "info@damac.com",
    "phone": "9876543211"
}
add_client(client_data_2)

# Create an agent for VaporVM
agent_vaporvm = create_agent("VaporVM")

# Test find similar companies tool
response_vaporvm = agent_vaporvm.invoke({
    "input": "Find similar companies to Du."
})
print(f"Agent Response: {response_vaporvm}")
