import pandas as pd

english_data = pd.read_csv("data/en.w3strings.csv", delimiter="|", header=None).iloc[:, 3:]
english_data.columns = ["en_text"]

polish_data = pd.read_csv("data/pl.w3strings.csv", delimiter="|", header=None).iloc[:, 3:]
polish_data.columns = ["pl_text"]

df = pd.concat([english_data, polish_data], axis=1)
df.to_csv("data/dataset.csv", sep="|", index=False)