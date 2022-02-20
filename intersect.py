from unicodedata import name
import pandas as pd

df1 = pd.read_csv('not_blur.csv', header=0, sep=',')
df2 = pd.read_csv('usable_face.csv', header=0, sep=',')

# print(df1["name"])
# print(df2["name"])
df2[df2["name"].isin(df1["name"])].to_csv('intersect.csv', header=["name", "width", "height"], index=None)
