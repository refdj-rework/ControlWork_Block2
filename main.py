import pandas as pd #импорт библиотеки
data = pd.read_excel('data.xlsx') #импорт таблицы

def co_str(a, b): #функция вывода ячейки
    print(data.iloc[a, b]) #вывод ячейки


while 1:
    try: #проверка на ошибки
        print("Напишите ")
        a = int(input("Введите номер столбца: ")) #Ввод столбца
        b = int(input("Введите номер строки: ")) #Ввод строки
        co_str(a, b) #Вызов функции
        passs = input("Нажмите ENTER чтобы продолжить или напишите EXIT для выхода...  ") #pass
        if passs.lower() == "exit": #выход
            break

    except: #если ошибка
        print("Ошибка!") #Вывод сообщения об ошибке