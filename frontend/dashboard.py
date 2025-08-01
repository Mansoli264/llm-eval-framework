import streamlit as st
import pandas as pd
import requests
import json

st.title("LLM Evaluation & Benchmarking Dashboard")

model1_output = st.text_area("Model 1 Outputs (JSON list)")
model2_output = st.text_area("Model 2 Outputs (JSON list)")
references = st.text_area("Ground Truth References (JSON list)")

if st.button("Evaluate"):
    payload = {
        "model_outputs": {
            "Model_1": json.loads(model1_output),
            "Model_2": json.loads(model2_output)
        },
        "references": json.loads(references)
    }
    res = requests.post("http://localhost:8000/evaluate", json=payload)
    st.json(res.json())
