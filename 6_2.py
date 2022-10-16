# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.


def numbers (n):
    data = [i for i in range(20, n +1) if i % 20 == 0 or i % 21 == 0]
    return data

n = int(input("Введите max число > "))
print(numbers(n))