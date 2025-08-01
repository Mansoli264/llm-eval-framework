from fastapi import FastAPI
from pydantic import BaseModel
from app.evaluator import evaluate_models

app = FastAPI()

class EvalRequest(BaseModel):
    model_outputs: dict
    references: list

@app.post("/evaluate")
async def evaluate(req: EvalRequest):
    results = evaluate_models(req.model_outputs, req.references)
    return results
