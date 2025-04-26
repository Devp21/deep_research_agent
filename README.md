# Deep Research Agent System

An **autonomous research agent** built using **LangChain**, **LangGraph**, and **Groq LLMs**.  
This agent takes a research topic, performs a search, fact-checks results, lists sources, and drafts a structured, human-like answer.

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/Devp21/deep_research_agent.git
cd deep_research_agent

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. **Install the Python packages**

```bash
pip install -r requirements.txt

4. **Install the Python packages**
Create a .env file in the project folder and add:

```dotenv
GROQ_API_KEY=your-groq-api-key
TAVILY_API_KEY=your-tavily-api-key
