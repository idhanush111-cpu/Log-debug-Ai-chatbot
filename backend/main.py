from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from src.retriever import LogRetriever
from src.log_analyzer import analyze_log

app = FastAPI()

# Allow React to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

retriever = None

@app.post("/upload-log")
async def upload_log(file: UploadFile = File(...)):
    global retriever

    content = await file.read()
    text = content.decode()

    retriever = LogRetriever(text)

    return {"status": "log loaded"}

@app.post("/ask")
async def ask_ai(question: dict):
    global retriever

    if retriever is None:
        return {"error": "Load log first"}

    q = question["question"]

    chunks = retriever.get_relevant_chunks(q)
    context = "\n\n".join(chunks)

    messages = [
        {"role": "system", "content": f"Relevant log:\n{context}"},
        {"role": "user", "content": q}
    ]

    answer = analyze_log(messages)

    return {
        "answer": answer,
        "evidence": chunks
    }
