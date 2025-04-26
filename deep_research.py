# deep_research.py

#imports
import os
from dotenv import load_dotenv
from typing import TypedDict

from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.graph import StateGraph

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")


search_tool = TavilySearchResults(k=5)
llm = ChatGroq(model="llama3-70b-8192", temperature=0.2)  

class ResearchState(TypedDict):
    query: str
    research_notes: str
    sources_list: str
    validated_notes: str
    drafted_answer: str


#Research agent
def research_agent(state: ResearchState) -> dict:
    query = state["query"]
    results = search_tool.run(query)
    summarized_notes = f"Summary of Search Results for '{query}':\n"
    for idx, res in enumerate(results):
        title = res.get('title', 'No Title')
        snippet = res.get('snippet', 'No Snippet Provided')
        summarized_notes += f"\n[{idx+1}] Title: {title}\nSnippet: {snippet}\n"
    return {"research_notes": summarized_notes}

# Source agent
def source_list_agent(state: ResearchState) -> dict:
    query = state["query"]
    results = search_tool.run(query)
    sources_summary = f"Sources for '{query}':\n"
    for idx, res in enumerate(results):
        title = res.get('title', 'No Title')
        link = res.get('url', 'No Link Provided')
        sources_summary += f"\n[{idx+1}] {title}\nLink: {link}\n"
    return {"sources_list": sources_summary}

#Factcheck agent
def fact_check_agent(state: ResearchState) -> dict:
    research_notes = state["research_notes"]
    fact_check_prompt = PromptTemplate.from_template("""
    You are a fact-checking AI. Review the following research notes.
    Remove anything outdated, inaccurate, or irrelevant.

    Research Notes:
    {research_notes}

    Return only clean, accurate, and relevant notes.
    """)
    fact_check_chain = fact_check_prompt | llm
    validated_notes = fact_check_chain.invoke({"research_notes": research_notes}).content
    return {"validated_notes": validated_notes}

#Drafting agent
def drafting_agent(state: ResearchState) -> dict:
    validated_notes = state["validated_notes"]
    draft_prompt = PromptTemplate.from_template("""
    Using the following validated research notes, draft a well-structured, detailed answer.

    Research Notes:
    {validated_notes}

    Answer should have:
    - An Introduction
    - Main Body
    - Conclusion
    """)
    draft_chain = draft_prompt | llm
    final_answer = draft_chain.invoke({"validated_notes": validated_notes}).content
    return {"drafted_answer": final_answer}

#graph
graph = StateGraph(ResearchState)

graph.add_node("research", research_agent)
graph.add_node("source_list", source_list_agent)
graph.add_node("fact_check", fact_check_agent)
graph.add_node("draft", drafting_agent)

graph.add_edge("research", "source_list")
graph.add_edge("source_list", "fact_check")
graph.add_edge("fact_check", "draft")

graph.set_entry_point("research")
graph.set_finish_point("draft")

compiled_graph = graph.compile()

#main
if __name__ == "__main__":
    user_query = input("Enter your research topic: ")
    output = compiled_graph.invoke({"query": user_query})

    print("\n📚 Final Structured Answer:\n")
    print(output["drafted_answer"])

    print("\n🔗 Sources Used:\n")
    print(output["sources_list"])