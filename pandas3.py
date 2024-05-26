import pandas as pd

df = pd.read_csv('animal.csv')
print(df)

# df.fillna(0, inplace=True) # заполняем пропуски нулями
# print(df)

df.dropna(inplace=True) # удаляем пропуски
print(df)

# group = df.groupby('Пища')['Средняя продолжительность жизни'].mean() # средняя продолжительность жизни по пище животного
# print(group)

df.to_csv('output.csv', index=False) # записываем в файл output.csv изменения
