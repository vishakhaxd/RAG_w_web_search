Here’s a clean, rewritten version of your **README** that highlights your addition of **RAG + web search**, while making the setup instructions clearer and more direct:

---

# 🔮 Gemini + RAG Fullstack LangGraph App

This project demonstrates a **fullstack AI research assistant** powered by **Google Gemini** and **LangGraph**, enhanced with a **Retrieval-Augmented Generation (RAG)** layer and integrated **web search**.

The system dynamically generates search queries, retrieves external and local knowledge, identifies knowledge gaps, and iteratively refines its reasoning to deliver a final, well-supported answer — complete with citations.

<img src="./app.png" title="Gemini Fullstack LangGraph" alt="Gemini Fullstack LangGraph" width="90%">

---

## 🚀 Features

* 🧠 **Gemini + RAG Agent** — combines Gemini models with a local/vector-based retrieval layer.
* 🌍 **Web Search Integration** — dynamically queries the web using Google Search API for fresh information.
* 🔁 **Iterative Research Loop** — identifies missing information and refines queries until sufficient coverage is achieved.
* 💬 **Fullstack Setup** — React frontend + LangGraph backend for a complete conversational experience.
* 🧩 **Hot Reloading** for both frontend and backend during development.

---

## 📂 Project Structure

* `frontend/`: React + Vite web app.
* `backend/`: FastAPI + LangGraph backend containing the Gemini RAG agent.

---

## ⚙️ Getting Started

### 1️⃣ Prerequisites

You’ll need:

* **Node.js (v18+)** and **npm** (or yarn/pnpm)
* **Python 3.11+**
* API Keys:

  * `GEMINI_API_KEY` (Google AI)
  * *(Optional)* `GOOGLE_SEARCH_API_KEY` for web search

---

### 2️⃣ Setup

#### Backend

```bash
cd backend
cp .env.example .env
# Add your keys
echo 'GEMINI_API_KEY="your_gemini_key"' >> .env
echo 'GOOGLE_SEARCH_API_KEY="your_search_key"' >> .env
pip install .
```

#### Frontend

```bash
cd frontend
npm install
```

---

### 3️⃣ Run Locally

Run both backend and frontend together:

```bash
make dev
```

Then open [http://localhost:5173/app](http://localhost:5173/app)

Or run them separately:

**Backend:**

```bash
cd backend
langgraph dev
```

→ API: [http://127.0.0.1:2024](http://127.0.0.1:2024)

**Frontend:**

```bash
cd frontend
npm run dev
```

→ UI: [http://localhost:5173](http://localhost:5173)

---

## 🧩 How It Works

The core agent (`backend/src/agent/graph.py`) follows this pipeline:

<img src="./agent.png" title="Agent Flow" alt="Agent Flow" width="50%">

1. **Initial Query Generation:** Uses Gemini to expand the user prompt into several targeted queries.
2. **Web & RAG Retrieval:** Fetches information from the web (Google Search API) and a local RAG vector store.
3. **Reflection Loop:** The agent reviews results, identifies knowledge gaps, and generates refined queries.
4. **Iteration:** Continues search and reflection until coverage is complete or iteration limit is reached.
5. **Answer Synthesis:** Produces a coherent answer with citations using Gemini.

---

## 💻 CLI Example

Run the research agent directly from the command line:

```bash
cd backend
python examples/cli_research.py "What are the latest trends in renewable energy?"
```

---

## 🐳 Deployment

For production deployment, the backend serves the optimized frontend build.

LangGraph requires **Postgres** (state + queue) and **Redis** (pub/sub).
Update your `.env` accordingly, then:

**Build the Docker image:**

```bash
docker build -t gemini-rag-langgraph -f Dockerfile .
```

**Run via docker-compose:**

```bash
GEMINI_API_KEY=<your_gemini_api_key> \
GOOGLE_SEARCH_API_KEY=<your_search_key> \
LANGSMITH_API_KEY=<your_langsmith_api_key> \
docker-compose up
```

→ App: [http://localhost:8123/app](http://localhost:8123/app)
→ API: [http://localhost:8123](http://localhost:8123)

---

## 🧰 Tech Stack

* **Frontend:** React (Vite) + Tailwind + Shadcn UI
* **Backend:** FastAPI + LangGraph + Gemini API
* **Retrieval:** FAISS / Chroma vector DB
* **Infra:** Redis, Postgres, Docker

---

## 📜 License

Licensed under Apache 2.0 — see [LICENSE](LICENSE).

---

Would you like me to include a short “RAG architecture diagram” section (showing Gemini + Web + Vector DB flow) to make the README more visually complete?
