import pandas as pd

df = pd.read_csv('hh.csv')
df['test'] = [ new for new in range(len(df)) ] # добавляем столбец test с новыми значениями в диапазоне длины датафрейма

print(df)

# df.drop(['test'], axis=1, inplace=True) # удаляем столбец test
df.drop(31, axis=0, inplace=True) # удаляем строку с индексом 31
print(df)   