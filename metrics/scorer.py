# metrics/scorer.py

import evaluate
from bert_score import score

def compute_bleu(preds, refs):
    metric = evaluate.load("bleu")
    return metric.compute(predictions=preds, references=[[ref] for ref in refs])["bleu"]

def compute_rouge(preds, refs):
    metric = evaluate.load("rouge")
    return metric.compute(predictions=preds, references=refs)["rougeL"]

def compute_bertscore(preds, refs):
    P, R, F1 = score(preds, refs, lang="en", verbose=False)
    return F1.mean().item()
