import pandas as pd

df0 = pd.read_csv('dz.csv')
print(df0)

df0['City'] = df0['City'].fillna('Cyty')
df0.fillna(0, inplace=True)
df0.to_csv('dz_not_NaN.csv', index=False)

df = pd.read_csv('dz_not_NaN.csv')
print(df)
group_cyty_1 = df.loc[df['City'] == 'Томск', 'Salary'].mean()
group_cyty_2 = df.loc[df['City'] == 'Москва', 'Salary'].mean()
print(f'Средня зарплата по городу Томск = {group_cyty_1:.2f}\nСредня зарплата по городу Москва = {group_cyty_2:.2f}')