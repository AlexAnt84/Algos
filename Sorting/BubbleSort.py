#Импортируем библиотеки
import copy
from ArrBasics import arr_fill

#Создадим 2 массива
arr_unsorted = []
arr_sorted = []

#Сортировка пузырьком
def arr_bubblesort (arr):
    arr = copy.deepcopy(arr)
    for i in range (0, len(arr) - 1):
        for j in range (0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j] = arr[j] + arr[j+1]
                arr[j+1] = arr[j] - arr[j+1]
                arr[j] = arr[j] - arr[j+1]
    return arr
                

#Основные действия
arr_unsorted = arr_fill (10, arr_unsorted)
print (arr_unsorted)
arr_sorted = arr_bubblesort (arr_unsorted)
print (arr_sorted)