import json
import pandas as pd

with open("sample.json") as f:
    data = json.load(f)

df = pd.json_normalize(data)
print(df)
