from agents.create_agent import create_agent

# Initialize the agent
agent = create_agent()

# Test enhanced recommendations
query = "Recommend services for Acme Corp."
response = agent.invoke({"input": query})

# Print the agent response
print("Agent Response:")
print(response)
