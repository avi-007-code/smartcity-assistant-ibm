import pandas as pd
from sklearn.ensemble import IsolationForest

# Summarize uploaded file (stub)
def summarize_file(file_content: str) -> str:
    lines = file_content.strip().splitlines()
    return f"File has {len(lines)} lines. First line: {lines[0] if lines else 'N/A'}"

# Detect anomalies in numeric columns (stub)
def detect_anomalies(df: pd.DataFrame) -> list:
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) == 0:
        return []
    model = IsolationForest(contamination=0.1, random_state=42)
    preds = model.fit_predict(df[numeric_cols])
    anomalies = df[preds == -1]
    return anomalies.index.tolist() 