from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
from tools.company_tools import find_similar_companies, recommend_client_services
from langchain.tools import Tool
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

def create_agent():
    # Define tools
    tools = [
        Tool(
            name="Find Similar Companies",
            func=find_similar_companies,
            description="Tool to find similar companies based on a company name."
        ),
        Tool(
            name="Recommend Services",
            func=recommend_client_services,
            description="Tool to recommend services for a client."
        )
    ]

    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=openai_api_key
    )

    # Initialize the Agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
    return agent
