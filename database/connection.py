import duckdb
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent



DB_PATH = BASE_DIR / "bengaluru.duckdb"



def get_connection():

    return duckdb.connect(

        str(DB_PATH)

    )