from posixpath import split
import random


def input_number_test_biger_then_zero(text: str) -> int:
    """Test - if input is a ineger > 0

    Args:
        text (str): input text - what shoul be writen bwfore input

    Returns:
        int: integer number that is > 0
    """
    int_test = True
    is_minus = False
    while int_test:
        number = input(f"{text}")  # ввод с описанием
        if number[
            0] == "-":  # проверка на <0 - если в начале есть символ "-" - сохраняет его в булевую переменную ( в данном случае не используется )
            is_minus = True
            number = number.replace("-",
                                    "")  # в данном случае - просто убирает 0 и сообщает что число стало положительным
            print("Entered number < 0 , remuved '-' ")
        if number.isdigit():  # если число формата integer - меняет ему тип
            number = int(number)
            if number == 0:
                print("Enter > 0")  # если число меньше 0 , не даёт закончить цикл и повторно просит ввести число
            else:
                int_test = False
        else:
            print("Not a number , try again")
    return number


def array_creation(length_of_array: int, min_for_random: int,
                   max_for_random: int) -> list:  # Создание списка из случайных чисел
    """Creation of array with random numbers

    Args:
        length_of_array (int): length of array
        min_for_random (int): minimum number in array
        max_for_random (int): maximum number in array

    Returns:
        list: array of random numbers
    """
    # простой цикл создания массива заданной длины и рандомом
    list_of_numbers = []
    for i in range(0, length_of_array):
        list_of_numbers.append(random.randint(min_for_random, max_for_random))
    return list_of_numbers


def array_creation_float(length_of_array: int, bit_depth=10, round_param=3) -> list:
    """cration of array with random float numbers

    Args:
        length_of_array (int): length of array
        bit_depth (int, optional): the length of number (digits) 10,100,1000 etc. Defaults to 10.
        round_param (int, optional): to waht ammoutn of numbers to round. Defaults to 3.

    Returns:
        list: _description_
    """
    # простой цикл создания массива дробных значений и затем перевод их в нужный формат
    list_of_numbers = []
    for i in range(0, length_of_array):
        list_of_numbers.append(round(random.random() * bit_depth,
                                     round_param))  # тут я понимаю что нужно проработать на сколько умножать - планирую продумать это в другой функции
    return list_of_numbers


def sum_of_not_numbers_in_array(list_of_numbers: list) -> int:
    """Counts sum of ellements thet are on not even positions

    Args:
        list_of_numbers (list): array in wich sum of ellements shuld ocure

    Returns:
        int: sum of elements
    """
    # если индекс не чётный - увеличивает сумму на значение под индексом
    sum = 0
    index = 0
    for i in list_of_numbers:
        # if list_of_numbers.index(i) % 2 == 0: # хотел по интересному сделать, но понял что штука не работает при двойных значениях =)
        if index % 2 != 0:
            sum += i
        index += 1

    return sum


def what_is_on_not_in_list(list_of_numbers: list) -> str:
    """Makes a text with elements on not even positions

    Args:
        list_of_numbers (list): array in wich non even positions will be looked up

    Returns:
        str: text fo elements
    """
    # пришлось сделать отдельную функцию для печати =) Первая итерация считает какое кол-во эллементов нужно быдует печатать
    result = ""
    count = 0
    index_main = 0
    for i in list_of_numbers:
        if index_main % 2 != 0:
            count += 1
        index_main += 1
    # вторая итеррация - пока счётсчик не дошёл до нужного кол-ва , в текст добавляет значений
    index = 0
    for i in list_of_numbers:
        if index_main % 2 != 0:
            index += 1
            result += str(i)
            if index < count:  # вот где используется кол-во эллементов - пока эллемент не последний , добавляет " и "
                result += " и "
        index_main += 1
    return result


def mult_of_par_in_list(list_of_numbers: list) -> list:
    """multiplication of pair in list (0,-1 / 1,-2 , etc)

    Args:
        list_of_numbers (list): array in wich multiplication will ocure

    Returns:
        list: list of multiplied pairs
    """
    # цикл проходит до середины массива - перемножает 1 и последний эллемент и добавляет результат в новый список
    list_fo_mult_pars = []
    for i in range(0, int(len(list_of_numbers) / 2)):
        list_fo_mult_pars.append(list_of_numbers[i] * list_of_numbers[-(i + 1)])
    # если кол-во эллементов не чётное - средний эллемент возводит в квадрат
    if len(list_of_numbers) % 2 != 0:
        list_fo_mult_pars.append(list_of_numbers[len(list_of_numbers) % 2 + 1] ** 2)
    return list_fo_mult_pars


def min_max_of_drob_in_list(list_of_numbers: list) -> int:
    """look up min and max value of fraction part in float numbers in array

    Args:
        list_of_numbers (list): array of float numbers

    Returns:
        int: min and max valuses
    """
    # проходит по спуску дробных чисел - оставляет только дробную часть и проверят - оно минимальное и проверяет оно максимальное
    max = list_of_numbers[0] - int(list_of_numbers[0])
    min = list_of_numbers[0] - int(list_of_numbers[0])
    for i in list_of_numbers:
        num = i - int(i)
        if num > max:
            max = num
        if num < min:
            min = num
    return min, max


def in_byte_transfer(number: int) -> list:
    """codes number in 2byte code

    Args:
        number (int): number that shoud be coded

    Returns:
        list: integer 2 byte code of number
    """
    ostatok = number
    list_of_bites = []
    # деление без остатка на 2 - это будущий остаток, Число - остаток = 1 или 0 для записпи в код
    # потом число меняет на остаток и повторяет процецц пока остаток больше 1
    while ostatok >= 1:
        ostatok = number // 2
        # print(number,ostatok,number-ostatok*2) # провкерка
        list_of_bites.append(number - ostatok * 2)
        number = ostatok
    sort_array(
        list_of_bites)  # разворачивает список ( кстати - пример Void функции - если я правильно понмю , в C# списки и массивы были ссылочными типами, по этому любое изменение - меняет его везед)
    return convert_list_in_int(list_of_bites)  # переводит списко в число ( сделал что бы было как в примере )


def sort_array(list_of_numbers: list):
    """Sorts array in back order

    Args:
        list_of_numbers (list): array to sort
    """
    # стандартный цикл разворота списка
    for i in range(0, int(len(list_of_numbers) / 2)):
        list_of_numbers[i], list_of_numbers[-(1 + i)] = list_of_numbers[-(1 + i)], list_of_numbers[i]
        # print(list_of_numbers) # провкерка


def convert_list_in_int(list_of_numbers: list) -> int:
    """converts list of numbers in to one integer

    Args:
        list_of_numbers (list): _description_

    Returns:
        int: _description_
    """
    # цикл перевода эллементов массива в 1 строчку, после чего переводит всё в число
    result = ""
    for i in list_of_numbers:
        result = result + str(i)
    return int(result)


def fibonachi_plus(fib_range: int) -> list:
    """makes array of fibonacci numbers > 0

    Args:
        fib_range (int): range of fibonacci numbers

    Returns:
        list: > 0 fibonacci array
    """
    flibonachi_list = [0, 1]
    if fib_range > 1:
        for i in range(2, fib_range + 1):
            # формула рассчёта фибоначи, для этог первые 2 числа записанны
            flibonachi_list.append(flibonachi_list[i - 1] + flibonachi_list[i - 2])
    return flibonachi_list


def fibonachi_minus(
        fib_range: int) -> list:  # наверное можно было обойтись без этого и просто каждый второй эллемент обычного фибоначи умнодить на -1, но подумал - вдруг когда то потребуется только минуосовй фибоначи
    """makes fibonacci numbers < 0

    Args:
        fib_range (int): range of fibonacci numbers

    Returns:
        list: < 0 fibonacci array
    """
    flibonachi_list = [0, 1]
    if fib_range > 1:
        for i in range(2, fib_range + 1):
            # формула рассчёта фибоначи, для этог первые 2 числа записанны
            flibonachi_list.append(flibonachi_list[i - 2] - flibonachi_list[i - 1])
    return flibonachi_list


def fibonachi_from_minus_to_plus(fib_range: int) -> list:
    """compels two fibonacci arrays ( < 0 and > 0 ) in one fibonacci array

    Args:
        fib_range (int): range of fibonacci

    Returns:
        list: list of fibonacci numbers
    """
    fib_plus = fibonachi_plus(fib_range)  # создаёт положителный фибоначи
    flibonachi_list = fibonachi_minus(fib_range)  # создаёт отрицательный фибоначи
    sort_array(flibonachi_list)  # разворачивает отрицательный фибоначи
    for i in range(1, fib_range + 1):  # к отрицательному добавляет положительный по каждому эллементу
        flibonachi_list.append(fib_plus[i])
    return flibonachi_list