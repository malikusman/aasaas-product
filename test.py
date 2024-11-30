# from database import engine, Base

# # Create tables
# Base.metadata.create_all(bind=engine)

# print("Tables created successfully.")


from crud import add_company, add_client, get_clients, add_recommendation, add_conversation

# Test: Add a company
company_data = {
    "name": "VaporVM",
    "email": "info@vaporvm.com",
    "contact_person": "John Doe",
    "phone": "1234567890",
    "website": "www.vaporvm.com"
}
company = add_company(company_data)
print(f"Company added: {company.name}")

# Test: Add a client
client_data = {
    "company_id": company.id,
    "name": "Du",
    "services_taken": "Cloud Management, Server Hosting",
    "why_with_us": "Trust and expertise",
    "website": "www.du.ae",
    "email": "info@du.ae",
    "phone": "9876543210"
}
client = add_client(client_data)
print(f"Client added: {client.name}")

# Test: Get clients
clients = get_clients(company.id)
for client in clients:
    print(f"Client: {client.name}, Services: {client.services_taken}")

# Test: Add a recommendation
recommendation_data = {
    "client_id": client.id,
    "similar_company": "Etisalat",
    "recommended_services": "Cloud Monitoring, Server Hosting"
}
recommendation = add_recommendation(recommendation_data)
print(f"Recommendation added: {recommendation.similar_company}")

# Test: Add a conversation
conversation = add_conversation(
    session_id="session123",
    user_input="Find similar companies to Du.",
    agent_output="Etisalat, STC"
)
print(f"Conversation logged: {conversation.user_input} -> {conversation.agent_output}")
