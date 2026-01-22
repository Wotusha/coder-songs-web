from flask import Flask, request, jsonify
from llama_cpp import Llama
import os

app = Flask(__name__)

# Load the Model (The Brain)
print("Loading Neural Core...")
llm = Llama(model_path="./my_neural_core.gguf", n_ctx=2048, verbose=False)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    # Generate Response
    output = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are a Private AI Assistant running on a dedicated server."},
            {"role": "user", "content": user_input}
        ]
    )
    return jsonify({"response": output['choices'][0]['message']['content']})

if __name__ == '__main__':
    # Run on port 10000 (Render's default)
    app.run(host='0.0.0.0', port=10000)
