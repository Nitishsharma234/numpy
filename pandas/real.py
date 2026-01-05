import pandas as pd

data = {
    "name": ["Amit", "Riya", "Karan", "Sneha", "Rahul"],
    "gender": ["Male", "Female", "Male", "Female", "Male"],
    "day": ["Mon", "Tue", "Mon", "Tue", "Mon"],
    "total_bill": [500, 700, 450, 800, 600],
    "tip": [50, 70, 45, 80, 60]
}

n = pd.DataFrame(data)
print(n)
print(n.groupby("day")["tip"].mean())
print(n.groupby("gender")["total_bill"].sum())
