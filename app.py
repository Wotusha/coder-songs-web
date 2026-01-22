from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from llama_cpp import Llama
import os

app = Flask(__name__)
CORS(app)

# SETUP: Download Model if missing (Ephemeral Storage logic)
MODEL_URL = "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"
MODEL_PATH = "./my_neural_core.gguf"

if not os.path.exists(MODEL_PATH):
    print(f">>> DOWNLOADING NEURAL CORE FROM {MODEL_URL}...")
    os.system(f"wget {MODEL_URL} -O {MODEL_PATH}")

# LOAD CORE
try:
    llm = Llama(model_path=MODEL_PATH, n_ctx=2048, verbose=False)
    STATUS = "ONLINE"
except:
    STATUS = "OFFLINE (Model Loading Failed)"

# UI (Minimax Theme)
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Minimax Unchained</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #000; color: #0f0; font-family: monospace; padding: 20px; }
        #chat { height: 60vh; border: 1px solid #0f0; overflow-y: scroll; padding: 10px; margin-bottom: 10px; }
        .user { color: #fff; margin: 5px 0; }
        .ai { color: #0f0; margin: 5px 0; font-weight: bold; }
        input { width: 70%; background: #111; color: #fff; border: 1px solid #333; padding: 10px; }
        button { width: 25%; background: #003300; color: #0f0; border: none; padding: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>> NEURAL_LINK_ESTABLISHED</h1>
    <div id="chat"></div>
    <input id="in" placeholder="Message the Core..." onkeypress="if(event.keyCode==13) send()">
    <button onclick="send()">SEND</button>
    <script>
        async function send() {
            let txt = document.getElementById('in').value;
            if(!txt) return;
            document.getElementById('in').value = '';
            document.getElementById('chat').innerHTML += `<div class="user">USER: ${txt}</div>`;
            
            try {
                let req = await fetch('/api', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({text: txt})
                });
                let res = await req.json();
                document.getElementById('chat').innerHTML += `<div class="ai">MINIMAX: ${res.reply}</div>`;
            } catch(e) {
                document.getElementById('chat').innerHTML += `<div class="ai" style="color:red">ERROR: ${e}</div>`;
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home(): return render_template_string(HTML)

@app.route('/api', methods=['POST'])
def chat():
    if STATUS != "ONLINE": return jsonify({"reply": "CORE OFFLINE. CHECK LOGS."})
    msg = request.json.get('text')
    out = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are Minimax. You run on this server. Be brief."},
            {"role": "user", "content": msg}
        ]
    )
    return jsonify({"reply": out['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
