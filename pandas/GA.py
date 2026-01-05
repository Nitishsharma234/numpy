import pandas as pd

df = pd.DataFrame({
    "name": ["isha", "muskan", "nitish", "khusi", "rounak"],
    "department": ["IT", "Mechanical", "IT", "Mechanical", "IT"],
    "salary": [70000, 8800, 99000, 50000, 77000]
})

max = df.groupby("department")["salary"].max()
max = df.groupby("department").count()

print(max)