import sys

def sorting(array):   # сортировка пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array1, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    else:
        middle = (right + left) // 2  # находимо середину
        if element == array1[middle]:  # СЕГМЕНТ 1
            return middle-1  # возвращаем  индекс элемента предшествуюшего середине
        elif element < array1[middle] and element <= array1[middle-1]:  # СЕГМЕНТ 2
            return binary_search(array1, element, left, middle-1)
        elif element < array1[middle] and element > array1[middle-1]: # СЕГМЕНТ 3
            return middle-1
        elif element > array1[middle] and element <= array1[middle+1]: # СЕГМЕНТ 4
            return middle
        elif element > array1[middle] and element > array1[middle+1]: # СЕГМЕНТ 5
            return binary_search(array1, element, middle+1, right)

print("Введите последовательность неповторяющихся целых чисел через пробел: ")
num_str = sys.stdin.readline()
num_str = num_str.replace('\n', '')
str_list = list(num_str.split(sep=' '))

# проверка на корректность введенных данных
try:
    num_list = list(map(int, str_list))
except ValueError as e:
    print(f"Не все введенные Вами данные являются числами. Повторите попытку запуска программы.")
else:
    print("Вы ввели последовательность чисел.")

# проверка на отсутствие повторяющихся элементов
set_num_list = set(num_list)
if len(num_list) != len(set_num_list):
    print("Во введенной последовательности есть повторяющиеся числа. Повторите попытку запуска программы.")
    quit()

sorted_list = sorting(num_list)

print("Введите любое целое число: ")
num = sys.stdin.readline()
# проверка, что пользователем введено целое число
try:
    num = int(num)
except ValueError as err:
    print(f"Вы ввели не число. Повторите попытку запуска программы.")
    quit()
else:
    print("Вы ввели корректные данные.")


print(f"Числовой ряд из Ваших чисел в отсортированном порядке: {sorted_list}.")

searched_element = binary_search(sorted_list, num, 0, len(sorted_list)-1)
print(f"Номер позиции элемента числового ряда, который меньше введенного Вами числа, а следующий за ним больше или равен этому числу: {searched_element}")
