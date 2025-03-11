import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


languages = pd.read_csv("./data/languages.csv")
# language_data={}
data = pd.DataFrame()
for language in languages["LANGUAGE"]:
    if data.empty:
        data = pd.read_csv(f"./data/1991/raw/{language} - Sheet1.csv", thousands=',', na_values='-', dtype={"AREA_NAME": str, "defaultdict":np.int64})[["AREA_NAME", "TOTAL_P"]].rename(columns={'TOTAL_P': F'{language.upper()}'}).set_index("AREA_NAME")
        continue
    data = data.join(pd.read_csv(f"./data/1991/raw/{language} - Sheet1.csv", thousands=',', na_values='-', dtype={"AREA_NAME": str, "defaultdict":np.int64})[["AREA_NAME", "TOTAL_P"]].rename(columns={'TOTAL_P': F'{language.upper()}'}).set_index("AREA_NAME"))
data = data.reset_index()
data["AREA_NAME"] = data["AREA_NAME"].map(lambda x: x.upper())
# data.sort_values(by="AREA_NAME")
data = data.set_index("AREA_NAME")
data = data.sort_index()


data.to_csv("./data/1991/processed/language-by-region.csv")

REGION_NAME="ANDHRA PRADESH"
region_data = data.loc[REGION_NAME].sort_values(ascending=False)
# print(sum(region_data.values))
region_data = region_data[:10]

plt.figure(figsize=(16,6))
plt.bar(x=region_data.index.to_list(), height=region_data.values)
# plt.yscale("log")
plt.savefig(f"./graphs/{REGION_NAME}-1991.png")
# print(x=data.loc[REGION_NAME], y=data.index.to_list())
