import pandas as pd
import numpy as np

df_2011 = pd.read_csv("./data/2011/processed/full-data.csv").set_index("AREA_NAME")
df_1991 = pd.read_csv("./data/1991/processed/full-data.csv").set_index("AREA_NAME")

rename_2011 = {}
for col in df_2011.columns:
    if col == "AREA_NAME":
        continue
    rename_2011[col] = col + "_2011"
df_2011.rename(columns=rename_2011, inplace=True)
rename_1991 = {}
for col in df_1991.columns:
    if col == "AREA_NAME":
        continue
    rename_1991[col] = col + "_1991"
df_1991.rename(columns=rename_1991, inplace=True)

df_combined = df_2011.join(df_1991)
df_combined = df_combined.dropna(subset=['TOTAL_1991'])
df_combined.to_csv("./data/combined.csv")