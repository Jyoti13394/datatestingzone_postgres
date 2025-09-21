def validate_schema(df, expected_schema: dict):
    actual_schema = dict(df.dtypes.astype(str))
    for col, dtype in expected_schema.items():
        if col not in actual_schema or dtype not in actual_schema[col]:
            return False
    return True


def validate_not_null(df, not_null_cols: list):
    for col in not_null_cols:
        if df[col].isnull().any():
            return False
    return True
