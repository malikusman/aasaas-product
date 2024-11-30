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
    Add a new conversation to the database and return it with loaded attributes.
    :param session_id: Session identifier
    :param user_input: User's input
    :param agent_output: Agent's output
    :return: Newly created conversation object
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
        # Explicitly load attributes before closing the session
        db.refresh(new_conversation)
        return new_conversation
    finally:
        db.close()

        





