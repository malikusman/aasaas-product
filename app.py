from agents.create_agent import create_agent

# Initialize the agent
agent = create_agent()

# First query
response1 = agent.invoke({"input": "Find similar companies to Acme Corp."})
print("Response 1:", response1)

# Second query with memory
response2 = agent.invoke({"input": "Now recommend services for Acme Corp."})
print("Response 2:", response2)
