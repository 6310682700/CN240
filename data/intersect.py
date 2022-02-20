import pandas as pd

df1 = pd.read_csv('legend.csv', header=0, sep=',')
df2 = pd.read_csv('intersect.csv', header=0, sep=',')

# print(df1["image"])
# print(df2)
df1[df1["image"].isin(df2["name"])].to_csv('legend-2.csv', header=["user.id","image","emotion"], index=None)
