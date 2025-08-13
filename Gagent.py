# agent.py
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from practice.tools import search_wikipedia

load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # You can also use gemini-pro-vision for multimodal
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

# Create the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run agent
query = input("Enter a topic to research: ")
response = agent.run(query)
print("\nAnswer\n", response)
