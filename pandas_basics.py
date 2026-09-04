import pandas as pd

student = [
    {
        "name" : "luffy",
        "age" : 19,
        "course" : "science",
        "marks" : 50
    },
    {
        "name" : "zoro",
        "age" : 20,
        "course" : "commerce",
        "marks" : 90
    },
    {
        "name" : "sanji",
        "age" : 21,
        "course" : "arts",
        "marks" : 90
    },
    {
        "name" : "robin",
        "age" : 23,
        "course" : "history",
        "marks" : 99
    },
    {
        "name" : "nami",
        "age" : 19,
        "course" : "geography",
        "marks" : 100
    }
]

df = pd.DataFrame(student)
# print(df)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
print(df[df["marks"] > 91])
# print(df["name"])