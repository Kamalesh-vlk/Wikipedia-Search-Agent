## 📚 Wikipedia Search Agent

This project demonstrates how to build an **AI-powered Wikipedia research assistant** using **Google Gemini** (via LangChain) and a custom Wikipedia search tool.

The agent can take any query, search Wikipedia for relevant information, and summarize the results into a concise, human-readable answer.

---

### 🚀 Features
- **Google Gemini Integration** – Uses `gemini-1.5-flash` for fast and accurate text generation.
- **Wikipedia Search Tool** – Retrieves summaries from Wikipedia using the `wikipedia` Python library.
- **LangChain Agent** – Automatically decides when and how to use the Wikipedia tool to answer your question.
- **Interactive CLI** – Enter any topic and get an instant summarized response.

---

## 🔑 API Key Setup

This project uses **Google Gemini API** for natural language processing and **Wikipedia API** for retrieving topic summaries.

Before running the project, you need to set your API key in a `.env` file.

1. Create a `.env` file in the project root directory.
2. Add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```
---
## 📄 Sample Output

```shell
Enter a topic to research: MS Dhoni

Answer
MS Dhoni is a former Indian professional cricketer, widely regarded as one of the greatest ODI batsmen and captains. 
He captained India in limited-overs formats from 2007 to 2017 and in Test cricket from 2008 to 2014. 
He led India to victory in the 2007 ICC World Twenty20, the 2011 Cricket World Cup, and the 2013 ICC Champions Trophy.
```

## ✅ Note:
To run the Wikipedia Search Agent with a Streamlit UI:
```
streamlit run Gagents.py
```
