import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Данные для графика
data = pd.read_excel('data.xlsx') #импорт таблицы

x = [1, 5, 10, 15, 20]



fst_line = []
fst_line = data.iloc[0, :]
scn_line = []
scn_line = data.iloc[:, 2]
# Создание графика

plt.figure(figsize=(12, 7))

plt.xlabel("Ось X")
plt.ylabel("Ось Y")

plt.plot(x, fst_line, scn_line)
plt.grid(True)
# Отображение графика
plt.show()


