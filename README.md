# 🧠 LLM Evaluation Framework: Ask Docs, Measure Answers

This project is an **LLM Evaluation Framework** designed to test how well large language models (LLMs) answer questions based on documents — like technical manuals, research papers, or product guides.

Imagine uploading a PDF, asking questions about it, and then seeing how accurate and helpful the LLM’s answers are. That’s exactly what this app does!

---

## ✨ Key Features

✅ **Ask Questions from Docs**  
Upload structured or unstructured content, ask questions, and get smart answers powered by LLMs.

✅ **Semantic Similarity Evaluation**  
We don't just stop at getting answers — we **score them** using **semantic similarity**. That means: does the model really understand the context?

✅ **Modular Design**  
- **Backend**: Built with FastAPI (clean REST APIs)  
- **Frontend**: Built with Streamlit (simple dashboard)  
- **Evaluation Engine**: Custom logic to evaluate model output  
- **Dockerized**: Easy to run anywhere (local or cloud)

---

## 🛠️ Tech Stack

| Layer         | Tools Used                            |
|---------------|----------------------------------------|
| Backend       | Python, FastAPI, Uvicorn               |
| Frontend      | Python, Streamlit                      |
| Evaluation    | SentenceTransformers, Semantic Scoring |
| Data Handling | JSON, RAG-style input chunks           |
| Deployment    | Docker, Docker Compose                 |

---

## 🚀 How It Works (In Simple Steps)

1. Upload a document or data source (`prompts.json`)  
2. The backend breaks it into chunks and prepares questions  
3. An LLM (e.g., GPT-4) gives answers  
4. We evaluate the answers based on similarity with ground truth  
5. The dashboard shows scores and insights

---

## 📁 Project Structure

llm-eval-framework/
│
├── backend/ → FastAPI backend
│ ├── app/ → Core logic (evaluation, API)
│ └── requirements.txt → Python deps for backend
│
├── frontend/ → Streamlit dashboard
│ └── requirements.txt → Python deps for frontend
│
├── metrics/ → Custom scorers (e.g., semantic similarity)
├── data/ → Sample inputs (like prompts.json)
├── docker-compose.yml → Combined app orchestration
├── README.md → This file 😄
└── .gitignore → Clean setup

yaml
Copy
Edit

---

## 🧪 Evaluation Metrics Used

- **Cosine Similarity** between embeddings (thanks to `SentenceTransformers`)
- **BLEU / ROUGE** (optional)
- Ground truth vs model answer comparisons

---

## 🧰 Running the Project (Local with Docker)

Make sure Docker is installed, then:

```bash
git clone https://github.com/Mansoli264/llm-eval-framework.git
cd llm-eval-framework
docker-compose up --build
This will spin up:

FastAPI backend at http://localhost:8000

Streamlit frontend at http://localhost:8501

🧠 Why This Project Matters
Whether you're building an AI assistant, chatbot, or RAG pipeline — evaluating model output is 🔑. This project gives you a plug-and-play evaluation engine you can improve and reuse anywhere.
Perfect for:
AI research
LLM fine-tuning
Real-world QA systems
Interviews or demo portfolios
