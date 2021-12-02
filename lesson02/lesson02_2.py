'''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
'''

ar_list = [1, -1, False, 1.1, 'True', None]
def fun_type(el):
    for el in range(len(ar_list)):
        print(type(ar_list[el]))
    return
fun_type(ar_list)

'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить
на своем месте.
Для заполнения списка элементов необходимо использовать
функцию input().
'''
ar_count = int(input("Введите количество элементов "))
arr = []
i = 0
el = 0
while i < ar_count:
    arr.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(arr)/2)):
        arr[el], arr[el + 1] = arr [el + 1], arr[el]
        el += 2
print(arr)

'''
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
'''
a_list = ['Зима', 'Весна', 'Лето', 'Осень']
a_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите номер месяца "))
if month==1 or month==2 or month==12:
    print(a_dict.get(1))
    print(a_list[0])
elif month==3 or month==4 or month==5:
    print(a_dict.get(2))
    print(a_list[1])
elif month==6 or month==7 or month==8:
    print(a_dict.get(3))
    print(a_list[2])
elif month==9 or month==10 or month==11:
    print(a_dict.get(4))
    print(a_list[3])
else:
        print("Некорректный номер")
'''
Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове.
'''
str_word = input("Введите строку ")
ar_word = []
print(str_word.split(' '))
ar_word = str_word.split(' ')
for el in range(len(ar_word)):
    if len(str(ar_word)) <= 10:
        print(f"{el+1}{' '}{ar_word[el]}")
    else:
        print(f"{el+1}{' '}{ar_word[el][0:10]}")

'''
Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться
после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, 
например, my_list = [7, 5, 3, 3, 2].
'''

number = int(input("Enter number: "))
my_list = [7, 5, 3, 3, 2]
c = my_list.count(number)
for element in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

'''
Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей. Каждый кортеж хранит информацию об
отдельном товаре. В кортеже должно быть два элемента —
номер товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя.
'''
goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода введите 'Q', для ввода данных - 'Enter', для аналитики -  'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Ввод характеристик "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))