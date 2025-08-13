import os
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from practice.tools import search_wikipedia

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="Wikipedia-Search-Agent", page_icon="🔍", layout="centered")

# Title
st.title("🔍 Wikipedia-Search-Agent")
st.write("Ask any question and let the agent search Wikipedia for answers!")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Define tools
tools = [
    Tool(
        name="Wikipedia Search",
        func=search_wikipedia,
        description="Useful for answering questions about people, places, or topics."
    )
]

# Create agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

# User input
query = st.text_input("Enter a topic to research:", "")

# Run search when user clicks button
if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Searching Wikipedia..."):
            response = agent.run(query)
        st.subheader("📄 Answer")
        st.write(response)
