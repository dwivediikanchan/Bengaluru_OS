from database.connection import get_connection




def get_jobs_data():


    conn = get_connection()



    data = conn.execute(

        """

        SELECT *

        FROM jobs

        LIMIT 100

        """

    ).fetchdf()



    conn.close()



    return data.to_dict(

        orient="records"

    )