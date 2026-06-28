from database.connection import get_connection
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2:3b")


def city_chat(query: str):

    conn = get_connection()

    # Pull small context from all tables
    housing = conn.execute("SELECT area, rent FROM housing").fetchdf()
    traffic = conn.execute("SELECT area, avg_speed FROM traffic").fetchdf()
    jobs = conn.execute("SELECT location as area, salary FROM jobs").fetchdf()
    civic = conn.execute("SELECT area, complaint_count FROM civic").fetchdf()

    conn.close()

    # Build compact context (IMPORTANT: avoid huge prompt)
    context = f"""
Housing:
{housing.head(5).to_string(index=False)}

Traffic:
{traffic.head(5).to_string(index=False)}

Jobs:
{jobs.head(5).to_string(index=False)}

Civic:
{civic.head(5).to_string(index=False)}
"""

    prompt = f"""
You are a Bengaluru city intelligence AI assistant.

Use the dataset below to answer user query.

DATA:
{context}

USER QUESTION:
{query}

Rules:
- Be precise
- Suggest best areas if asked
- Compare areas if needed
- Keep answer under 8 lines
"""

    try:
        response = llm.invoke(prompt)

        return {
            "query": query,
            "answer": response
        }

    except Exception as e:

        return {
            "query": query,
            "answer": "AI not responding",
            "error": str(e)
        }