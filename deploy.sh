#!/bin/bash
# Minimax Neural Core Deployment Script
# Target: *.space.minimax.io

echo "======================================"
echo "MINIMAX NEURAL CORE DEPLOYMENT"
echo "======================================"
echo ""
echo "Target Domain: neural-core.space.minimax.io"
echo "Source: /workspace/final_core.py"
echo "Model: /workspace/my_neural_core.gguf"
echo ""

# Check if files exist
if [ ! -f "final_core.py" ]; then
    echo "ERROR: final_core.py not found!"
    exit 1
fi

if [ ! -f "my_neural_core.gguf" ]; then
    echo "ERROR: my_neural_core.gguf not found!"
    exit 1
fi

echo "✓ Files validated"
echo "✓ Ready for deployment"
echo ""
echo "To deploy to .space.minimax.io, run:"
echo "  kubectl apply -f deployment/k8s-deployment.yaml"
echo ""
echo "Or manually deploy to your hosting platform."
echo ""
echo "Your subdomain will be:"
echo "  neural-core.space.minimax.io"
echo ""
echo "======================================"

