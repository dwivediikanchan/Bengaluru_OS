from collections import Counter
import duckdb


def get_top_market_skills():

    conn = duckdb.connect(
        "database/bengaluru.duckdb"
    )

    df = conn.execute(
        "SELECT skills FROM jobs"
    ).fetchdf()

    conn.close()

    all_skills = []

    for skill_list in df["skills"]:

        skills = skill_list.split(",")

        all_skills.extend(
            [s.strip().lower()
             for s in skills]
        )

    skill_counts = Counter(
        all_skills
    )

    return list(
        skill_counts.keys()
    )