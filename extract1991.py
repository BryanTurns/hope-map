import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

languages = pd.read_csv("./data/languages.csv")
data = pd.DataFrame()
for language in languages["LANGUAGE"]:
    if data.empty:
        data = pd.read_csv(f"./data/1991/raw/{language} - Sheet1.csv", thousands=',', na_values='-', dtype={"AREA_NAME": str, "defaultdict":np.int64})[["AREA_NAME", "TOTAL_P"]].rename(columns={'TOTAL_P': F'{language.upper()}'}).set_index("AREA_NAME")
        continue
    data = data.join(pd.read_csv(f"./data/1991/raw/{language} - Sheet1.csv", thousands=',', na_values='-', dtype={"AREA_NAME": str, "defaultdict":np.int64})[["AREA_NAME", "TOTAL_P"]].rename(columns={'TOTAL_P': F'{language.upper()}'}).set_index("AREA_NAME"))
data = data.reset_index()
data["AREA_NAME"] = data["AREA_NAME"].map(lambda x: x.upper())
data = data.set_index("AREA_NAME").fillna(0)
data = data.sort_index()

data["TOTAL"] = data.sum(axis=1)
for col in data.columns:
    if col == "TOTAL":
        continue
    data[f"{col.strip()}_P"] = data[col] / data["TOTAL"]

data.to_csv("./data/1991/processed/full-data.csv")

REGION_NAME="ANDHRA PRADESH"
region_data = data.loc[REGION_NAME].sort_values(ascending=False)
region_data = region_data[:10]