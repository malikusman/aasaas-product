from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from tools.company_tools import find_similar_companies, recommend_client_services
from langchain.tools import Tool
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

def create_agent(client_name: str):
    # Define tools
    tools = [
        Tool(
            name=f"Find Similar Companies {client_name}",
            func=find_similar_companies,
            description=f"Find similar companies based on the client's name: {client_name}"
        ),
        Tool(
            name=f"Recommend Services for {client_name}",
            func=recommend_client_services,
            description=f"Recommend services specific to {client_name}"
        )
    ]

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=openai_api_key
    )
    
    # Add memory
    memory = ConversationBufferMemory(memory_key=f"{client_name}_chat_history")

    # Initialize the Agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
        memory=memory
    )
    return agent
