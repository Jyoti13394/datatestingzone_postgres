import pandas as pd
from sqlalchemy import create_engine


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def load_csv_to_postgres(csv_file, table_name, conn_string):
    df = pd.read_csv(csv_file, encoding="latin1")
    clean_df = clean_columns(df)
    engine = create_engine(conn_string)
    clean_df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"{len(clean_df)} records are loaded successfully into table {table_name} ")


# csv_file = "..\data\Sample - Superstore.csv"
# conn_string = "postgresql://postgres.rkxbktkiwgzcaksrcalw:[YOUR-PASSWORD]@aws-1-ap-south-1.pooler.supabase.com:6543/postgres"
# load_csv_to_postgres(csv_file, "superstore_data", conn_string)

