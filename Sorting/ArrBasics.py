#Функция заполнит массив случайными числами
import random, copy

def arr_fill (n, arr):
    arr = copy.deepcopy(arr)
    for i in range (0,n):
        arr.append(random.randint(0,100))
    return arr

    