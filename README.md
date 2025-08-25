# 🧠 Truthscribe – AI Blog Generator (CrewAI)

Generate **fact-checked, well-cited blog articles** using a multi-agent AI system.  
Truthscribe orchestrates multiple specialized agents (Research, Validation, Writing, Citation) to ensure **accuracy, readability, and transparency**.

---

## ✨ Features

- 🔎 **Research Agent** – Finds trusted, reputable sources (via Serper + Wikipedia).  
- ✅ **Validator Agent** – Verifies facts against memory & Wikipedia, rejecting unverifiable claims.  
- ✍️ **Writer Agent** – Produces clean, structured blog posts (Markdown format).  
- 📑 **Citation Agent** – Attaches inline citations and builds references.  
- 🧠 **Fact Memory** – Stores validated facts using ChromaDB + embeddings for reuse.  
- 🎨 **Streamlit UI** – User-friendly interface with topic input and fact injection.  

---

## 🧰 Tech Stack

| Tool / Library         | Role |
|------------------------|------|
| **CrewAI**             | Multi-agent orchestration |
| **Cohere LLM**         | Language model backend |
| **Sentence-Transformers** | Embedding model for fact memory |
| **ChromaDB**           | Persistent memory store |
| **Wikipedia + Serper** | Research + fact validation sources |
| **Streamlit**          | Frontend interface |

---

## 🏗️ How It Works

The workflow is an **agent pipeline**:

```text
Topic → Research Agent → Validator Agent → Writer Agent → Citation Agent → Blog Output
```

- **Research Agent**: Finds facts with citations.  
- **Validator Agent**: Cross-checks each claim (memory + Wikipedia).  
- **Writer Agent**: Generates draft with only validated content.  
- **Citation Agent**: Ensures proper inline citations.  
- **Fact Memory**: Stores verified facts for future use.  

---

## 📁 Project Structure

```
├── app.py               # Streamlit UI
├── crew_builder.py      # Orchestrates multi-agent workflow
├── agents/              # Agent definitions
│   ├── research_agent.py
│   ├── validator_agent.py
│   ├── writer_agent.py
│   └── citation_agent.py
├── core/                # Core tools
│   └── tools.py
├── utils/               # Fact memory, helpers
│   └── fact_memory.py
├── .env.example         # Example environment file
├── requirements.txt     # Dependencies
└── README.md            # Project docs
```

---

## 🚀 Run It Locally

Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/yourusername/ai-blog-generator.git
cd ai-blog-generator
python -m venv myenv
source myenv/bin/activate   # or .\myenv\Scripts\activate on Windows
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

Rename `.env.example` → `.env` and add keys:

```env
COHERE_API_KEY=your_cohere_key
SERPER_API_KEY=your_serper_key   # optional if using Serper
```

---

## ⚠️ Notes

- Articles are **fact-based only** – unverifiable claims are discarded.  
- Some **very recent events** may not appear if not on Wikipedia or trusted sites.  
- Memory is **persistent** (ChromaDB), so validated facts are reusable.  

---

## 📄 License

MIT License — free to use, fork, and extend.  

🙌 Contributions are welcome! Open an **issue** for bugs/suggestions or a **pull request** to improve the project.  

---

👉 Tagline: *“Let the agents do the fact-checking. You just pick the topic.”*
