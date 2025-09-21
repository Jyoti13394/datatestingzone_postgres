import psycopg2
from psycopg2 import OperationalError


class DBConnection:
    def __init__(self, host, dbname, user, password, port):
        try:
            self.conn = psycopg2.connect(
                host=host,
                dbname=dbname,
                user=user,
                password=password,
                port=port,
                sslmode="require"
            )
            self.conn.autocommit = True
            print("Connected to Postgres")
        except OperationalError as e:
            print("Connection Error:", e)
            self.conn = None

    def run_query(self, query):
        if not self.conn:
            print(" No active DB Connection")
            return None
        try:
            with self.conn.cursor() as curr:
                curr.execute(query)
                try:
                    return curr.fetchall()
                except psycopg2.ProgrammingError:
                    return None
        except Exception as e:
            print("Query Error:", e)
            return None

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection Closed")


# db = DBConnection(
#     host="aws-1-ap-south-1.pooler.supabase.com",
#     dbname="postgres",
#     user="postgres.rkxbktkiwgzcaksrcalw",
#     password="Maldives786#",
#     port=6543
# )
#
# query = "SELECT * FROM superstore_data where ship_mode = 'Second Class' limit 5"
# print(db.run_query(query))
# db.close()