import pandas as pd 

n = {"salary" :[70000,8800,99000,00,77000],"department": ["IT","Mechanical","IT","mevh","mech"],"name" : ["isha","muskan","nitish","khusi","rounak"]}
new = pd.DataFrame({"salary":[10000],"department":["IT"],"name":["jay"]})
df = pd.DataFrame(n)
df = pd.concat([df,new])

print(df[df["department"]=="IT"])
print(df[df["salary"]>50000])

print(df[["salary","name"]])