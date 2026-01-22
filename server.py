from flask import Flask, request, jsonify
from llama_cpp import Llama

app = Flask(__name__)
# Load the Model
llm = Llama(model_path="./my_neural_core.gguf", n_ctx=2048, verbose=False)

@app.route('/', methods=['POST'])
def home():
    msg = request.json.get('text')
    output = llm.create_chat_completion(
        messages=[{"role": "user", "content": msg}]
    )
    return jsonify({"reply": output['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
