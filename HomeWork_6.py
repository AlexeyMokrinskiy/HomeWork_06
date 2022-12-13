'''
1. предложить улучшения кода для четырёх уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension'''

'''
3.1. Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
## Оригинал
# from random import Random, randint

# size = int(input('Введите размер списка '))
# min_value = int(input('Введите минимальное значение '))
# max_value = int(input('Введите максимальное значение '))

# random_list = []
# for i in range(size):
#     random_list.append(randint(min_value, max_value))
# print('Наш список', random_list)

# odd_list = random_list[1::2]
# print('Hа нечётных позициях элементы', odd_list)

# sum = 0
# for i in range(len(odd_list)):
#     sum += odd_list[i]
# print('Oтвет:', sum)

'''map на ввод чисел с консоли'''

# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# sum_odd_index(lst)

'''
3.2. Задайте список. Напишите программу, которая определит, присутствует ли в
заданном списке строк некое число.
['22', '33', '123', 'fwefe', 'ytyy', '55']
'''

## Оригинал:
# our_list = ['22', '33', '123', 'fwefe', 'ytyy', '55']
# u = 55

# for i in range(len(our_list)):
#     if our_list[i].isdigit() and int(our_list[i]) == u:
#         print(f'В списке присутсвует искомое значение на позиции {i}')

'''lambda'''
# our_list = ['22', '33', '123', 'fwefe', 'ytyy', '55']
# u = '55'
# res = list(filter(lambda x: u in x, our_list))

# print(res)

'''
4.3. Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
'''
## оригинал (решил не правильно)
# from random import Random, randint

# size = int(input('Введите размер списка '))

# random_list = []
# for i in range(size):
#     random_list.append(randint(0, 5)) 
# print('при ', random_list, '->', end=' ')

# new_list = []
# for i in random_list:
#     if i not in new_list:
#         new_list.append(i)

# print(new_list)

'''list comprehension'''
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

'''
5.1. Напишите программу, удаляющую из файла все слова, содержащие "абв".
'''
##Оригинал
# my_text = "авыаывлдо вфыафыа абвафлыафл авьтабв ывфыы"

# find_text = "абв"

# def text_remover(lst, rt):
#     lst1= []
#     for i in lst.split():
#         if rt not in i:
#             lst1.append(i)
#     return lst1

# print(text_remover(my_text, find_text))

'''lambda&filter'''
# my_text = "авыаывлдо вфыафыа абвафлыафл авьтабв ывфыы"

# find_text = "абв"
# list_word2 = list(filter(lambda x: find_text not in x, my_text.split()))
# print(' '.join(list_word2))


'''
2* Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
приоритет операций стандартный.
Добавьте возможность использования скобок, меняющих приоритет операций.
    *Пример:* 
    1+2*3 => 7; 
    (1+2)*3 => 9;

''' 
# Эту я не доделал
# a = '2 - 9 + 20 / 2 + 3 * 7'
# def split_string(string):
#     string = string.replace('+', ' + ')
#     string = string.replace('-', ' - ')
#     string = string.replace('/', ' / ')
#     string = string.replace('*', ' * ')
#     return string.split()

# print(split_string(a))

# def calc_parce(digit_lst):
#     new_list = []
#     for i in range(len(digit_lst)):
#         if digit_lst[i].isdigit() and i > 0:
#             digit_lst[i] = float(digit_lst[i])
#             if digit_lst[i - 1] == '+':
#                 new_list.append(digit_lst[i])
#             elif digit_lst[i -1] == '-':
#                 new_list.append(digit_lst[i] * -1)
#             elif digit_lst[i -1] == '*':
#                 new_list.append(digit_lst[i] * new_list[-1])
#             elif digit_lst[i -1] == '/':
#                 new_list.append(digit_lst[i] / new_list[-1])
#         elif digit_lst[i].isdigit() and i == 0:
#             digit_lst[i] = float(digit_lst[i])
#             new_list.append(digit_lst[i])
#     return sum(new_list)

# print(calc_parce(split_string(a)))

