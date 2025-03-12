import pandas as pd
import numpy as np
import os


my_data = pd.DataFrame()
my_data["AREA_NAME"] = []
my_data["LANGUAGE"] = []
my_data["TOTAL_P"] = []
my_data =my_data.astype({"AREA_NAME": object})
my_data =my_data.astype({"LANGUAGE": object})
my_data =my_data.astype({"TOTAL_P": np.int64})

my_data = my_data.set_index(["AREA_NAME", "LANGUAGE"])

i  = 0
for f_name in os.listdir('./data/2011/raw'):
\
    data = pd.read_excel(f'./data/2011/raw/{f_name}', 'Sheet1', index_col=None)
    data = data[["Unnamed: 4", "Unnamed: 6", "Unnamed: 7"]]

    data = data.rename(columns={"Unnamed: 4": "AREA_NAME", "Unnamed: 6":"LANGUAGE", "Unnamed: 7": "TOTAL_P"}).drop([0, 1, 2, 3, 4])
    data = data[data["LANGUAGE"].str.fullmatch("^[0-9].*")]
    data = data[data["AREA_NAME"].str.contains("Other") == False]

    region = data["AREA_NAME"].values[0]
    data= data[data["AREA_NAME"].str.fullmatch(region)]
    data["LANGUAGE"] = data.loc[:, ("LANGUAGE")].str.split(' ', n=1).str[1]
    data = data.astype({"TOTAL_P": np.int64})
    data = data.set_index(["AREA_NAME", "LANGUAGE"])

    my_data = pd.concat([data, my_data])
    i += 1

my_data = my_data.reset_index()
regions = my_data["AREA_NAME"].unique()

data = {}
for language in my_data["LANGUAGE"].unique():
    data[language] = []
data["AREA_NAME"] = []
final_df = pd.DataFrame(data)
for region in my_data["AREA_NAME"].unique():
    region_data = my_data.set_index("AREA_NAME").loc[region].values

    cols = {}
    cols["AREA_NAME"] = region
    for language in region_data:
        cols[language[0]] = language[1]

    final_df.loc[len(final_df)] = cols

final_df = final_df.set_index("AREA_NAME").fillna(0).sort_index()

final_df["TOTAL"] = final_df.sum(axis=1)
for col in final_df.columns:
    if col == "TOTAL":
        continue
    final_df[f"{col}_P"] = final_df[col] / final_df["TOTAL"]
print(final_df)
final_df.to_csv("./data/2011/processed/full-data.csv")

