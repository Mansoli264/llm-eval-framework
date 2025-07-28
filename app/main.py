from fastapi import FastAPI, UploadFile, File
from app.evaluator import evaluate_all_metrics
import pandas as pd
import io

app = FastAPI()

@app.post("/evaluate/")
async def evaluate_files(ground_truth: UploadFile = File(...), responses: UploadFile = File(...)):
    gt_df = pd.read_csv(io.BytesIO(await ground_truth.read()))
    res_df = pd.read_csv(io.BytesIO(await responses.read()))
    result = evaluate_all_metrics(gt_df, res_df)
    return result

@app.get("/")
def health_check():
    return {"message": "LLM Evaluation Framework is running!"}
