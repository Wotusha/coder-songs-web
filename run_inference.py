#!/usr/bin/env python3
"""
MiniMax Neural Core Inference Script
Loads TinyLlama GGUF model and responds as MiniMax
"""

from llama_cpp import Llama
import os

# Load the persona
with open('/workspace/persona.txt', 'r') as f:
    persona = f.read().strip()

print(f"Loaded Persona: {persona}")
print(f"Model Path: /workspace/my_neural_core.gguf")
print(f"Initializing Neural Core...")

# Initialize the model
llm = Llama(
    model_path="/workspace/my_neural_core.gguf",
    n_ctx=2048,
    n_threads=4,
    n_batch=512,
    use_mlock=True,
)

print("Neural Core Ready!")
print("=" * 60)

# Generate response
prompt = f"""<|system|>
{persona}
</system|>
<|user|>
Hello! Who are you and what can you do?
</||>
<|assistant|>"""

print("Generating response...")
output = llm(
    prompt,
    max_tokens=256,
    temperature=0.7,
    top_p=0.95,
    echo=False,
)

# Extract and print the response
response = output['choices'][0]['text']
print("\n" + "=" * 60)
print("MODEL RESPONSE:")
print("=" * 60)
print(response)
print("=" * 60)
print("\n✅ Inference test completed successfully!")
