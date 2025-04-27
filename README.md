# 🔍 AI Research Assistant | LangGraph + Groq + Tavily

![Workflow](https://img.shields.io/badge/Workflow-LangGraph-blue) 
![LLM](https://img.shields.io/badge/LLM-Llama3--70B-orange) 
![Search](https://img.shields.io/badge/Search-Tavily-green)

An automated research pipeline that fetches, validates, and drafts structured answers with sources using LangGraph and Groq's Llama3-70B.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- API keys: [Groq](https://console.groq.com/) + [Tavily](https://app.tavily.com/)

```bash
# Clone and setup
git clone https://github.com/yourusername/research-assistant.git
cd research-assistant
pip install -r requirements.txt

# Add keys to .env
echo "GROQ_API_KEY=your_key_here" > .env
echo "TAVILY_API_KEY=your_key_here" >> .env

# Run
python deep_research.py


## 🧩 Workflow

1. **User Input**
   - User enters a **research topic** they want information on.

2. **Research Agent (Searcher)**
   - Crawls the web using **Tavily API** to collect relevant, real-time data.
   - Returns top articles, summaries, and sources.

3. **Fact-Checking Agent**
   - Analyzes the gathered information.
   - Validates facts, removes inconsistencies or unreliable sources.

4. **Drafting Agent**
   - Organizes the verified information.
   - Drafts a **structured, coherent, human-like** research report.

5. **Final Output**
   - Displays a well-organized answer along with a **list of references**.
   - (Optional) Can save or export the results later.
---
