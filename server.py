from flask import Flask, request, jsonify
from agents.create_agent import create_agent

app = Flask(__name__)
agent = create_agent()

@app.route('/chat', methods=['POST'])
def chat():
    """
    Chat endpoint for the user to interact with the agent.
    """
    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({"error": "Query is required"}), 400
    
    response = agent.invoke({"input": user_query})
    return jsonify({"response": response['output']})

if __name__ == "__main__":
    app.run(debug=True)
