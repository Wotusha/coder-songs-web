# Minimax Neural Core Deployment to .space.minimax.io

## Deployment Configuration

### Domain: *.space.minimax.io

### Required Files:
1. final_core.py - Flask server application
2. my_neural_core.gguf - Neural model (638MB)
3. requirements.txt - Python dependencies

### Kubernetes Resources Created:
- Deployment: minimax-neural-core
- Service: minimax-neural-core  
- Ingress: minimax-neural-core

### Subdomain: neural-core.space.minimax.io

