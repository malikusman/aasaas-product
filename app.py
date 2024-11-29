from agents.create_agent import create_agent

# Initialize the agent
agent = create_agent()

# Test the agent
query = "Find similar companies to XYZ Corp and recommend services for them."
response = agent.invoke({"input": query})

# Print the agent response
print("Agent Response:")
print(response)
