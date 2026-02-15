# Log-debug-Ai-chatbot
Log Debug AI — RAG Powered Log Analysis Assistant
📌 Project Overview

Log Debug AI is an AI-powered log debugging assistant that uses Retrieval Augmented Generation (RAG) to analyze large system and network logs and answer debugging questions intelligently.

Instead of sending entire logs to AI models, this system:

Splits logs into chunks

Converts chunks into embeddings

Stores embeddings in a vector database

Retrieves only relevant log sections

Sends those sections to the AI model for reasoning

This makes the system:

✅ Fast
✅ Scalable
✅ Cost Efficient
✅ Accurate

🏗 Architecture
LOG FILE
   ↓
Chunking (log_chunker.py)
   ↓
Embeddings (vector_store.py)
   ↓
FAISS Vector Database
   ↓
User Question (app.py)
   ↓
Similarity Search (retriever.py)
   ↓
Relevant Log Context
   ↓
AI Model (GitHub Hosted / OpenAI Compatible)
   ↓
Final Answer (log_analyzer.py)

📂 Project Structure
Log-debug-Ai-chatbot/
│
├ backend/
│   └ main.py
│
├ src/
│   ├ chat_session.py
│   ├ log_chunker.py
│   ├ vector_store.py
│   ├ retriever.py
│   ├ log_analyzer.py
│
├ app.py
├ .env
├ requirements.txt
└ README.md

⚙️ Requirements
🐍 Python Version

Recommended:

Python 3.10 – 3.12

📦 Python Libraries

Core dependencies:

streamlit
fastapi
uvicorn
python-dotenv
numpy
faiss-cpu
openai

🚀 FULL INSTALLATION GUIDE (START TO END)
1️⃣ Clone Repository
git clone <YOUR_REPO_URL>
cd Log-debug-Ai-chatbot

2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Mac / Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

Using requirements:

pip install -r requirements.txt


OR manual install:

pip install streamlit fastapi uvicorn python-dotenv numpy faiss-cpu openai

4️⃣ Setup Environment Variables

Create .env file in project root.

Example (GitHub Models):

GITHUB_TOKEN=your_token_here


OR OpenAI Direct:

OPENAI_API_KEY=your_key_here

🧠 FULL PIPELINE EXPLANATION (END TO END EXECUTION)
▶ When You Run
streamlit run app.py

STEP 1 — Streamlit Starts Server

Streamlit:

Starts web server

Loads app.py

Initializes session state

STEP 2 — UI + Session Objects Created

File:

app.py


Creates:

ChatSession → Stores chat history
Retriever → Initially None
Vector Store → Not built yet

STEP 3 — User Loads Log

Flow:

app.py
 → retriever.py
 → log_chunker.py
 → vector_store.py

🔹 Log Chunking

File:

log_chunker.py


Function:

chunk_log(text, chunk_size)


Purpose:
Split large logs into manageable pieces.

Output:

List of log chunks

🔹 Embeddings Generation

File:

vector_store.py


Function:

create_embeddings()


Purpose:
Convert log text into vector numbers.

Why:
Allows semantic similarity search.

🔹 FAISS Vector Database Creation

File:

vector_store.py


Creates FAISS index:

faiss.IndexFlatL2


Stores:

Vector → Log Chunk Mapping


This step happens ONLY once per log load.

STEP 4 — User Asks Question

File:

app.py


Example:

Why did firmware upgrade fail?

STEP 5 — Similarity Search

Flow:

app.py
 → retriever.py
 → vector_store.py


Process:

Convert question → embedding

Search FAISS index

Return most similar log chunks

STEP 6 — Context Building

File:

app.py


Creates AI input context:

Relevant Log Chunks + User Question

STEP 7 — AI Reasoning

File:

log_analyzer.py


Calls AI model:

client.chat.completions.create()


Uses:

System Prompt

Retrieved Log Context

User Question

STEP 8 — Answer Generation

AI generates human readable debugging explanation.

STEP 9 — Chat Memory Storage

File:

chat_session.py


Stores:

User question

AI response

DATA TRANSFORMATION FLOW
Raw Input
Full Log Text


↓

Chunking
Log → Smaller Segments


↓

Embedding
Text → Vector Numbers


↓

Vector Database
Searchable Memory Index


↓

Query Search
Question → Matching Log Segments


↓

AI Reasoning
Context + Question → Answer

🖥 Running The Application
Run Streamlit UI
streamlit run app.py


Open browser:

http://localhost:8501



⭐ Key Features
 RAG Based Log Analysis

Only relevant logs sent to AI.

 Scalable To Large Logs

FAISS vector search enables fast retrieval.

 Chat Memory Support

Maintains debugging conversation context.

 Modular Architecture

Easy to extend and upgrade.

 FUTURE ROADMAP :-

V5

Testcase Intelligence Layer
Failure Pattern Learning
Automated RCA Generation