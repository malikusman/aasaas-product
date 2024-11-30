import datetime
from database import SessionLocal, Company, Client, Recommendation, Conversation

def add_company(company_data):
    """
    Add a new company to the database.
    :param company_data: dict with company fields (e.g., name, email, etc.)
    :return: Newly created company object
    """
    db = SessionLocal()
    try:
        new_company = Company(**company_data)
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        return new_company
    finally:
        db.close()
        

def add_client(client_data):
    """
    Add a new client to the database.
    :param client_data: dict with client fields (e.g., name, company_id, etc.)
    :return: Newly created client object
    """
    db = SessionLocal()
    try:
        new_client = Client(**client_data)
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client
    finally:
        db.close()

def get_clients(company_id):
    """
    Get all clients for a specific company.
    :param company_id: ID of the company
    :return: List of clients
    """
    db = SessionLocal()
    try:
        return db.query(Client).filter_by(company_id=company_id).all()
    finally:
        db.close()
        
def add_recommendation(recommendation_data):
    """
    Add a recommendation for a client.
    :param recommendation_data: dict with recommendation fields (e.g., client_id, similar_company, etc.)
    :return: Newly created recommendation object
    """
    db = SessionLocal()
    try:
        new_recommendation = Recommendation(**recommendation_data)
        db.add(new_recommendation)
        db.commit()
        db.refresh(new_recommendation)
        return new_recommendation
    finally:
        db.close()
        
def add_conversation(session_id, user_input, agent_output):
    """
    Add a new conversation to the database.
    """
    db = SessionLocal()
    try:
        new_conversation = Conversation(
            session_id=session_id,
            user_input=user_input,
            agent_output=agent_output
        )
        db.add(new_conversation)
        db.commit()
        db.refresh(new_conversation)  # Ensure attributes are loaded
        return new_conversation
    finally:
        db.close()

def get_conversation_history(client_name: str):
    """
    Retrieve all chat history for a specific client.
    """
    db = SessionLocal()
    try:
        return db.query(Conversation).filter(Conversation.session_id.like(f"{client_name}_%")).all()
    finally:
        db.close()

def save_conversation(client_name: str, user_input: str, agent_output: str):
    """
    Save a conversation for a specific client.
    """
    session_id = f"{client_name}_{datetime.datetime.now().isoformat()}"
    return add_conversation(
        session_id=session_id,
        user_input=user_input,
        agent_output=agent_output
    )


        





