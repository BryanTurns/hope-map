import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_combined = pd.read_csv("./data/combined.csv")
df_combined = df_combined.set_index("AREA_NAME")
cols_p2011 = df_combined.columns.str.contains("_P_2011")
cols_p1991 = df_combined.columns.str.contains("_P_1991")
df_p2011 = df_combined.loc[:, cols_p2011]
df_p1991 = df_combined.loc[:, cols_p2011]

assam = df_combined.loc["ASSAM"]
print(assam)
# Convert cols into key

# plt.bar(x=df_c)

# plt.figure(figsize=(16,6))
# plt.bar(x=region_data.index.to_list(), height=region_data.values)
# plt.yscale("log")
# plt.savefig(f"./graphs/{REGION_NAME}-1991.png")
# print(x=data.loc[REGION_NAME], y=data.index.to_list())
