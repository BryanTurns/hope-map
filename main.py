import pandas as pd

data = pd.read_csv("./2011.csv")
print(data["MOTHER_TONGUE_NAME"])
data = data[data["MOTHER_TONGUE_NAME"]==" Assamese"]

print(data)