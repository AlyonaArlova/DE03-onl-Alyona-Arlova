import pandas as pd
import numpy as np

df = pd.read_csv("/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW8/sales.csv")
print(df)

df['random_price'] = np.random.randint(2000, 5000, size = len(df))
print(df)

#фильтрация
expensive = df[df['random_price'] > 3000]  # Фильтрует товары с финальной ценой больше 3000
print('Самый дорогой товар: ', expensive)

low_price = df[df['random_price'] < 3000]  # Фильтрует товары с финальной ценой меньше 3000
print('Самый дешевый товар: ',low_price)
#сортировка
sorted_df = df.sort_values(by='random_price', ascending=False)  # Сортирует DataFrame по столбцу 'final_price' в порядке убывания
print('Сортировка по random_price (по убыванию): ', sorted_df)

#агрегация
max_price = df.groupby('category')['random_price'].max()  # Находит максимальную цену в каждой категории
print('Максимальное значение: ', max_price)
