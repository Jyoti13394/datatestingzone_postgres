import pytest
import pandas as pd
from src.db_connection import DBConnection

"""Created just to explain"""


# @pytest.fixture(scope="session")
# def sample_df():
#     print("Creating sample dataframe")
#     return pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})


@pytest.fixture(scope="session")
def db():
    """DB Connection for session"""
    conn = DBConnection(host="aws-1-ap-south-1.pooler.supabase.com",
                        dbname="postgres",
                        user="postgres.rkxbktkiwgzcaksrcalw",
                        password="Maldives786#",
                        port=6543,
                        )
    yield conn
    conn.close()


@pytest.fixture(scope="session")
def superstore_csv():
    """Load source csv"""
    return pd.read_csv("..\data\Sample - Superstore.csv", encoding="latin1")


# @pytest.fixture(scope="session")
# def test_cases_file():
#     """Load Excel-Driven test cases"""
#     return pd.read_excel("..\\data\\test_cases.xlsx")
