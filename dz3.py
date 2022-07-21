# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import All_functions_for_home_work as AF
#
# def sum_of_not_numbers_in_array(list_of_numbers:list) -> int:
#     """Counts sum of ellements thet are on not even positions
#     Args:
#         list_of_numbers (list): array in wich sum of ellements shuld ocure
#     Returns:
#         int: sum of elements
#     """
#     # если индекс не чётный - увеличивает сумму на значение под индексом
#     sum = 0
#     index = 0
#     for i in list_of_numbers:
#         # if list_of_numbers.index(i) % 2 == 0: # хотел по интересному сделать, но понял что штука не работает при двойных значениях =)
#         if index % 2 != 0:
#             sum += i
#         index += 1
#
#     return sum
#
# def what_is_on_not_in_list(list_of_numbers:list) -> str:
#     """Makes a text with elements on not even positions
#     Args:
#         list_of_numbers (list): array in wich non even positions will be looked up
#     Returns:
#         str: text fo elements
#     """
#     # пришлось сделать отдельную функцию для печати =) Первая итерация считает какое кол-во эллементов нужно быдует печатать
#     result = ""
#     count = 0
#     index_main = 0
#     for i in list_of_numbers:
#         if index_main % 2 != 0:
#             count += 1
#         index_main += 1
#     # вторая итеррация - пока счётсчик не дошёл до нужного кол-ва , в текст добавляет значений
#     index = 0
#     for i in list_of_numbers:
#         if index_main % 2 != 0:
#             index += 1
#             result += str(i)
#             if index < count: # вот где используется кол-во эллементов - пока эллемент не последний , добавляет " и "
#                 result += " и "
#         index_main += 1
#     return result
#
#
# list_of_numbers = AF.array_creation(10,1,10)
# sum = sum_of_not_numbers_in_array(list_of_numbers)
# print_elements = what_is_on_not_in_list(list_of_numbers)
# print(f"{list_of_numbers} -> на нечётных позициях элементы {print_elements}, ответ:{sum}")


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# import All_functions_for_home_work as AF
#
# def mult_of_par_in_list(list_of_numbers : list) -> list:
#     """multiplication of pair in list (0,-1 / 1,-2 , etc)
#     Args:
#         list_of_numbers (list): array in wich multiplication will ocure
#     Returns:
#         list: list of multiplied pairs
#     """
#     # цикл проходит до середины массива - перемножает 1 и последний эллемент и добавляет результат в новый список
#     list_fo_mult_pars = []
#     for i in range (0,int(len(list_of_numbers)/2)):
#         list_fo_mult_pars.append(list_of_numbers[i] * list_of_numbers[-(i+1)])
#     # если кол-во эллементов не чётное - средний эллемент возводит в квадрат
#     if len(list_of_numbers) % 2 != 0:
#         list_fo_mult_pars.append(list_of_numbers[len(list_of_numbers) % 2+1] ** 2)
#     return list_fo_mult_pars
#
#
# list_of_numbers = AF.array_creation(6,1,10)
# list_of_results = mult_of_par_in_list(list_of_numbers)
#
# print(f"{list_of_numbers} => {list_of_results}")


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import All_functions_for_home_work as AF
#
# def min_max_of_drob_in_list(list_of_numbers : list) -> int:
#     """look up min and max value of fraction part in float numbers in array
#     Args:
#         list_of_numbers (list): array of float numbers
#     Returns:
#         int: min and max valuses
#     """
#     # проходит по спуску дробных чисел - оставляет только дробную часть и проверят - оно минимальное и проверяет оно максимальное
#     max = list_of_numbers[0] - int(list_of_numbers[0])
#     min = list_of_numbers[0] - int(list_of_numbers[0])
#     for i in list_of_numbers:
#         num = i - int(i)
#         if num > max:
#             max = num
#         if num < min:
#             min = num
#     return min,max
#
# list_of = AF.array_creation_float(10)
#
# min,max = min_max_of_drob_in_list(list_of)
# dif = max - min
# print(f"{list_of} => max({max:.3f}) - min({min:.3f}) = {dif:.3f}")


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# import All_functions_for_home_work as AF
#
# def in_byte_transfer(number : int) -> list:
#     """codes number in 2byte code
#     Args:
#         number (int): number that shoud be coded
#     Returns:
#         list: integer 2 byte code of number
#     """
#     ostatok = number
#     list_of_bites =[]
#     # деление без остатка на 2 - это будущий остаток, Число - остаток = 1 или 0 для записпи в код
#     # потом число меняет на остаток и повторяет процецц пока остаток больше 1
#     while ostatok >= 1:
#         ostatok = number // 2
#         # print(number,ostatok,number-ostatok*2) # провкерка
#         list_of_bites.append(number-ostatok*2)
#         number = ostatok
#     AF.sort_array(list_of_bites) # разворачивает список ( кстати - пример Void функции - если я правильно понмю , в C# списки и массивы были ссылочными типами, по этому любое изменение - меняет его везед)
#     return AF.convert_list_in_int(list_of_bites) # переводит списко в число ( сделал что бы было как в примере )
#
# number = AF.input_number_test_biger_then_zero("Enter number > 0 : ")
# result = in_byte_transfer(number)
# print(f" - {number} -> {result}")