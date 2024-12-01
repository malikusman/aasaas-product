from flask import Flask, request, jsonify
from agents.create_agent import create_agent
from crud import add_conversation, get_conversation_history

app = Flask(__name__)

# Create agents for clients (this can be dynamic in a real-world app)
agents = {
    "VaporVM": create_agent("VaporVM"),
    "WehsiTravels": create_agent("WehsiTravels"),
}

# usman@Ihsanulhaqs-MBP ~ % curl -X POST http://127.0.0.1:5000/chat \
# -H "Content-Type: application/json" \
# -d '{"client": "VaporVM", "query": "Find similar companies to Du"}'
# {
#   "response": "Similar companies to Du are Etisalat and STC. Services recommended for Du include Cloud Hosting."
# }

@app.route('/chat', methods=['POST'])
def chat():
    """
    Chat endpoint for interacting with agents.
    """
    data = request.get_json()
    client_name = data.get('client', '')
    user_query = data.get('query', '')

    if not client_name or not user_query:
        return jsonify({"error": "Both 'client' and 'query' are required"}), 400

    # Get the agent for the client
    agent = agents.get(client_name)
    if not agent:
        return jsonify({"error": f"No agent found for client '{client_name}'"}), 404

    # Process the query
    try:
        response = agent.invoke({"input": user_query})
        # Save the conversation
        add_conversation(
            session_id=f"{client_name}_{request.remote_addr}",
            user_input=user_query,
            agent_output=response['output']
        )
        return jsonify({"response": response['output']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# curl http://127.0.0.1:5000/history\?client=VaporVM
@app.route('/history', methods=['GET'])
def history():
    """
    Retrieve chat history for a client.
    """
    client_name = request.args.get('client', '')
    if not client_name:
        return jsonify({"error": "'client' parameter is required"}), 400

    try:
        history = get_conversation_history(client_name)
        return jsonify({"history": [
            {"timestamp": conv.timestamp, "user_input": conv.user_input, "agent_output": conv.agent_output}
            for conv in history
        ]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/clients/add_agent', methods=['POST'])
def add_agent():
    """
    Add a new agent for a client.
    """
    data = request.get_json()
    client_name = data.get('client_name', '')

    if not client_name:
        return jsonify({"error": "'client_name' is required"}), 400

    # Check if the agent already exists
    if client_name in agents:
        return jsonify({"error": f"Agent for client '{client_name}' already exists"}), 400

    # Create a new agent
    agents[client_name] = create_agent(client_name)
    return jsonify({"message": f"Agent for client '{client_name}' created successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)
