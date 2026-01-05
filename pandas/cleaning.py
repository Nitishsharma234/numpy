import pandas as pd 


n = pd.DataFrame({"salary":[8000,78000],"name":["nitish","kumar","muskan"]})

n["salary"] = n["salary"].fillna(n["salary"].mean(),inplace=True)

print(n)