import sys
import os

# Make sure the root directory is in Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.evaluator import evaluate_models

if __name__ == "__main__":
    # ✅ Define predictions from multiple models
    model_outputs = {
        "GPT-4": ["AI is when machines try to act smart like humans."],
        "Gemini": ["Artificial Intelligence refers to machines imitating human intelligence."]
    }

    # ✅ Ground truth
    references = ["Artificial Intelligence is the simulation of human intelligence by machines."]

    # ✅ Run evaluation
    result = evaluate_models(model_outputs, references)
    
    # ✅ Output results
    print("Evaluation Results:")
    for model, metrics in result.items():
        print(f"\n🔹 {model}")
        for metric_name, score in metrics.items():
            print(f"  {metric_name}: {score:.4f}")
