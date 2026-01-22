from flask import Flask, request, jsonify, render_template_string
from llama_cpp import Llama

app = Flask(__name__)

# Load the Brain
print("Loading AI Model...")
llm = Llama(model_path="./my_neural_core.gguf", n_ctx=2048, verbose=False)

# The HTML Interface (Frontend)
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>My Private AI</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background: #f0f2f5; }
        #chat-box { height: 400px; overflow-y: scroll; background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid #ddd; }
        .msg { margin: 10px 0; padding: 10px; border-radius: 10px; width: fit-content; max-width: 80%; }
        .user { background: #0084ff; color: white; margin-left: auto; }
        .ai { background: #e4e6eb; color: black; }
        input { width: 70%; padding: 10px; border-radius: 5px; border: 1px solid #ddd; }
        button { width: 25%; padding: 10px; background: #0084ff; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <h2>Neural Core Chat</h2>
    <div id="chat-box"></div>
    <div style="display:flex; justify-content:space-between;">
        <input type="text" id="inp" placeholder="Type a message...">
        <button onclick="send()">Send</button>
    </div>
    <script>
        async function send() {
            let txt = document.getElementById('inp').value;
            if(!txt) return;
            
            // Show User Message
            document.getElementById('chat-box').innerHTML += `<div class="msg user">${txt}</div>`;
            document.getElementById('inp').value = '';
            
            // Send to Server
            let req = await fetch('/api', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: txt})
            });
            let res = await req.json();
            
            // Show AI Message
            document.getElementById('chat-box').innerHTML += `<div class="msg ai">${res.reply}</div>`;
            let box = document.getElementById('chat-box');
            box.scrollTop = box.scrollHeight;
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/api', methods=['POST'])
def api():
    user_input = request.json.get('text')
    output = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return jsonify({"reply": output['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10001)
