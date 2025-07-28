from nltk.translate.bleu_score import sentence_bleu
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_bleu(reference, prediction):
    return sentence_bleu([reference.split()], prediction.split())

def compute_similarity(reference, prediction):
    embeddings = model.encode([reference, prediction])
    return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

def evaluate_all_metrics(gt_df, res_df):
    results = []
    for i in range(len(gt_df)):
        ref = gt_df.iloc[i]['answer']
        pred = res_df.iloc[i]['answer']
        bleu = compute_bleu(ref, pred)
        sim = compute_similarity(ref, pred)
        results.append({
            "question": gt_df.iloc[i]['question'],
            "bleu": round(bleu, 4),
            "similarity": round(sim, 4)
        })
    return results
