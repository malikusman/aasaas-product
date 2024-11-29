from agents.create_agent import create_agent

# Initialize the agent
agent = create_agent()

# Test the agent
query1 = "Recommend services for XYZ Corp."
response1 = agent.invoke({"input": query1})

# Print the response
print("Agent Response (Recommendation):")
print(response1)

query2 = "Find similar companies to Acme Corp."
response2 = agent.invoke({"input": query2})

# Print the response
print("Agent Response (Find Similar):")
print(response2)
