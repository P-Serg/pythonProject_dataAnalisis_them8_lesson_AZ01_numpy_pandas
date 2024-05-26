import pandas as pd

df = pd.read_csv('mushroom_cleaned.csv')

# print(df.head())
print(df.info(), df.describe())