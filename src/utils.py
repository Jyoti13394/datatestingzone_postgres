import pandas as pd


def validate_not_null(df, not_null_cols: list):
    for col in not_null_cols:
        if df[col].isnull().any():
            return False
    return True


def yearly_order_drop_status(superstore_csv, db_result):
    """CSV Calculation"""
    superstore_csv["Year"] = (superstore_csv["Order Date"].astype(str).str.split(f"[/-]").str[-1].astype(int))

    csv_orders = (superstore_csv.groupby("Year")["Order ID"].count().reset_index(name = "total orders"))
    csv_orders["pct_change"] = csv_orders["total orders"].pct_change().fillna(0).round(4)
    csv_stats = dict(zip(csv_orders["Year"], csv_orders["pct_change"]))

    """Postgres Calculation"""
    db_df = pd.DataFrame(db_result, columns = ["year", "total_orders"])
    db_df["pct_change"] = db_df["total_orders"].pct_change().fillna(0).round(4)

    db_stats = dict(zip(db_df["year"], db_df["pct_change"]))

    print(f"CSV Status is: {csv_stats}")
    print(f"DB Status is: {db_stats}")

    #Compare
    if db_stats == csv_stats:
        print("Year over year growth stats match (CSV Vs DB)")
        return True
    else:
        print("Mismatch found")
        return False

