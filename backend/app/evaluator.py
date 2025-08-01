from metrics import scorer  # ✅ Correct absolute import

def evaluate_models(model_outputs, references):
    scores = {}
    for model, outputs in model_outputs.items():
        scores[model] = {
            "bleu": scorer.compute_bleu(outputs, references),
            "rouge": scorer.compute_rouge(outputs, references),
            "bertscore": scorer.compute_bertscore(outputs, references),
        }
    return scores
