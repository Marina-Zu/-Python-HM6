# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

from random import sample

def array (num):
    num = num if num > 0 else -num
    arr = sample(range(1, num* 2), num)
    print(arr)
    return arr

def big_num (array):
    data = [array[i+1] for i in range(len(array) - 1) if array[i] < array[i + 1]]
    return data


n = int(input("Введите количество элементов > "))
print(big_num(array(n)))