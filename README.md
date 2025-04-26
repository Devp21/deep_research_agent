# Deep Research Agent System

An **autonomous research agent** built using **LangChain**, **LangGraph**, and **Groq LLMs**.  
This agent takes a research topic, performs a search, fact-checks results, lists sources, and drafts a structured, human-like answer.

---

Setup Instructions 🛠️
If you want to run it locally, here’s what you need to do:

Clone the repo:
bash
git clone https://github.com/yourusername/deep_research_agent.git
cd deep_research_agent

(Optional) Create a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install the Python packages:
bash
pip install -r requirements.txt

Set up your API keys:
Create a .env file in the project folder and add:
dotenv
GROQ_API_KEY=your-groq-api-key
TAVILY_API_KEY=your-tavily-api-key
