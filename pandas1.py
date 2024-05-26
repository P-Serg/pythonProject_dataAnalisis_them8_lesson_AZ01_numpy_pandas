import pandas as pd

# data = [1, 2, 3, 4, 5] # данные
# series = pd.Series(data) # серийная структура
# print(series)

# data = {
#     'Name': ['John', 'Jane', 'Bob', 'Emily'],
#     'Age': [25, 30, 35, 40],
#     'City': ['New York', 'Paris', 'London', 'Moscow']
# } # словарь с данными
#
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv('World-happiness-report-2024.csv')
# print(df.head()) # первые 5 строк
# print(df.tail()) # последние 5 строк
# print(df.info()) # информация
# print(df.describe()) # статистика

# print(df['Country name']) # выбор столбца
# print(df[['Country name', 'Regional indicator']]) # выбор нескольких столбцов
# print(df[df['Ladder score'] > 7.5]) # выбор по условию
# print(df.loc[56]) # выбор по индексу
# print(df.iloc[56, 'Healthy life expectancy']) # выбор по индексу и столбцу
print(df[df['Healthy life expectancy']>0.7].head() # выбор по условию и вывод первых 5 строк
