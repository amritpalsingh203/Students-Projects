# Margdarshak Chatbot

## Team

Prashant Prabhakar - 21103112 - [prash240303](https://github.com/prash240303)

Abhay Mishra - 21103112 - [abhaymishra9](https://github.com/abhaymishra9)


## Description
Margdarshak is an intelligent academic assistant built with Retrieval-Augmented Generation (RAG). It allows users to ask questions related to uploaded PDFs/Excel sheets, with responses backed by relevant document context and source links. Designed for robust academic or enterprise use, it features a user-facing chatbot and an admin dashboard to manage knowledge sources.


## 🚀 Features

### 🔍 Chatbot (User Interface)
- Ask questions in natural language.
- Uses **RAG** to retrieve document context.
- Answers are powered by **LLMs** (e.g., *Mistral*, *LLaMA3*).
- Displays original **source link** for answer transparency.

### 🛠️ Admin Dashboard
- Upload **PDF** or **Excel** files via UI.
- Assign a **source link** (e.g., official URL or reference).
- Automatically stores files in **Amazon S3**.
- Files are processed, embedded, and indexed in a **vector database**.

### ⚙️ Backend (FastAPI)
- Handles file processing and chatbot logic.
- Extracts **embeddings** from PDF/Excel documents.
- Stores embeddings and metadata (incl. source link) in **vector DB**.
- `/chat` endpoint:
  - Converts question to embeddings.
  - Retrieves relevant document chunks.
  - Sends context + question to LLM.
  - Returns **answer + PDF source link**.


## Tech Stack

**Frontend:** React, TailwindCSS

**Backend:** FastAPI, Python, Langchain SDK

**Database & Storage:** ChromaDB

## Run Locally

Clone the project

```bash
git clone https://github.com/prash240303/major-project.git
```

### Frontend

Go to Frontend

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Run the project

```bash
npm start
```

Open http://localhost:3175 in browser

### Backend

Go to the backend folder:

```bash
cd backend

#Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

#Run the FastAPI server
uvicorn app.main:app --reload


### Backend
GROQ_API_KEY=
NOMIC_API_KEY=
AWS_S3_BUCKET_NAME=
S3_EXCEL_PREFIX=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=

### Frontend
VITE_BACKEND_URL=""

## Contributing
We welcome contributions! Feel free to fork, open issues, or submit pull requests.


## deployed backend 
"https://13.201.193.233:8000" or "margdarshak.tech/docs"

## Authors
- [Prashant](https://www.linkedin.com/in/prashant2403/)

- [Abhay](https://www.linkedin.com/in/abhaymishra99/)

