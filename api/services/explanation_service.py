from database.connection import get_connection
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2:3b")


def explain_area(area_name: str):

    conn = get_connection()

    housing = conn.execute(f"""
        SELECT * FROM housing
        WHERE LOWER(area) LIKE LOWER('%{area_name}%')
        LIMIT 1
    """).fetchdf()

    traffic = conn.execute(f"""
        SELECT * FROM traffic
        WHERE LOWER(area) LIKE LOWER('%{area_name}%')
        LIMIT 1
    """).fetchdf()

    jobs = conn.execute(f"""
        SELECT * FROM jobs
        WHERE LOWER(location) LIKE LOWER('%{area_name}%')
        LIMIT 1
    """).fetchdf()

    civic = conn.execute(f"""
        SELECT * FROM civic
        WHERE LOWER(area) LIKE LOWER('%{area_name}%')
        LIMIT 1
    """).fetchdf()

    conn.close()

    # ------------------------
    # Build raw data safely
    # ------------------------

    raw = []

    if not housing.empty:
        raw.append(f"Rent: {housing['rent'].values[0]}")

    if not traffic.empty:
        raw.append(f"Traffic: {traffic['avg_speed'].values[0]}")

    if not jobs.empty:
        raw.append(f"Salary: {jobs['salary'].values[0]}")

    if not civic.empty:
        raw.append(f"Civic issues: {civic['complaint_count'].values[0]}")

    # ------------------------
    # Fallback if no data
    # ------------------------

    if len(raw) == 0:
        return {
            "area": area_name,
            "reason": ["No data found for this area"]
        }

    # ------------------------
    # AI Prompt
    # ------------------------

    prompt = f"""
You are a Bengaluru city AI assistant.

Explain why this area is good or bad:

AREA: {area_name}

DATA:
{chr(10).join(raw)}

Give a short 3-5 line human explanation.
"""

    try:
        ai_response = llm.invoke(prompt)

        return {
            "area": area_name,
            "reason": raw,
            "ai_explanation": ai_response
        }

    except Exception as e:

        return {
            "area": area_name,
            "reason": raw,
            "ai_explanation": "AI model not responding",
            "error": str(e)
        }