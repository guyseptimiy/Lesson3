# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

# определяем свою функцию макс на три значения
def my_max(n1, n2, n3):
    return max(n1, max(n2, n3))


# вводим исходные данные
num1, num2, num3 = [int(s) for s in input('1 2 3:').split()]

# выводим максимальное введенное значение
print(my_max(num1, num2, num3))
