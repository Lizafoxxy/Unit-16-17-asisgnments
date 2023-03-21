import sys

def sorting(array):   # сортировка пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(L, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if element == L[middle]:  # если элемент в середине,
        return middle-1  # возвращаем этот индекс
    elif element < L[middle] and element < L[middle-1]:  # если элемент меньше элемента в середине
                                # и меньше предыдущего перед серединой, то рекурсивно ищем в
                                # левой половине
        return binary_search(L, element, left, middle-1)
    elif element > L[middle] and element <= L[middle+1]:
        return middle
    elif element > L[middle] and element > L[middle+1]:
        return binary_search(L, element, middle+1, right)

print("Введите последовательность целых чисел через пробел: ")
num_str = sys.stdin.readline()
num_str = num_str.replace('\n', '')
str_list = list(num_str.split(sep=' '))

# проверка на корректность введенных данных
try:
    num_list = list(map(int, str_list))
except ValueError as e:
    print(f"Не все введенные Вами данные являются числами. Повторите попытку запуска программы.")
else:
    print("Вы ввели корректные данные.")

sorted_list = sorting(num_list)

print("Введите любое число: ")
num = sys.stdin.readline()
try:
    num = int(num)
except ValueError as err:
    print(f"Вы ввели не число. Повторите попытку запуска программы.")
else:
    print("Вы ввели корректные данные.")


print(f"Ваши числа в отсортированном порядке: {sorted_list}.")

searched_element = binary_search(sorted_list, num, 0, len(sorted_list)-1)
print(f"Номер позиции элемента, который меньше введенного Вами числа, а следующий за ним больше или равен этому числу: {searched_element}")
