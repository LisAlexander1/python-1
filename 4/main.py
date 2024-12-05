import pandas as pd
import matplotlib.pyplot as plt
#Задание №13

data = {
    "№": [1, 2, 3, 4, 5, 6, 7],
    "ФИО": ["Иванова", "Петрова", "Сидорова", "Печкина", "Речкина", "Ивенков", "Петренков"],
    "Пол": ["ж", "ж", "ж", "ж", "ж", "м", "м"],
    "Класс": [2, 2, 2, 3, 3, 1, 1],
    "Количество баллов": [21, 20, 21, 21, 21, 20, 21],
    "Рост": [123, 138, 125, 140, 126, 134, 129]
}

df = pd.DataFrame(data)

# Отображаем таблицу
print(df)

# 1.
print('\nЗадание 1')
df_sorted = df.sort_values(by="Класс", ascending=False)
print(df_sorted)

# 2.
print('\nЗадание 2')
girls_3_class = df[(df["Класс"] == 3) & (df["Пол"] == "Ж")]
print(girls_3_class)

# 3.
print('\nЗадание 3')
mean_heights = df.groupby("Класс")["Рост"].mean()
print(mean_heights)

# 4.
print('\nЗадание 4')
pivot_table = pd.pivot_table(df, values="ФИО", index="Класс", columns="Пол", aggfunc="count", fill_value=0)
print(pivot_table)

# 5.
print('\nЗадание 5')
girls_2_class = df[(df["Класс"] == 2) & (df["Пол"] == "ж")]
print(girls_2_class)

# 6.
plt.figure(figsize=(8, 6))
plt.hist(df["Количество баллов"], bins=5, color='skyblue', edgecolor='black')
plt.title('Распределение количества баллов')
plt.xlabel('Количество баллов')
plt.ylabel('Частота')
plt.grid(True)
plt.show()