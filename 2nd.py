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



# x = [1, 5, 10, 15, 20]
# y1 = [1, 7, 3, 5, 11]
# y2 = [4, 3, 1, 8, 12]
#
# plt.figure(figsize=(12, 7))
#
# plt.plot(x, y1, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=2, ms=10)
# plt.plot(x, y2, 'v-.g', label="second", mec='r', lw=2, mew=2, ms=12)
# plt.legend()
# plt.grid(True)
# plt.show()

