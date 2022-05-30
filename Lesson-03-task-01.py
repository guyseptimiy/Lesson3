# . Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# определдяем функцию деления
def mydevide(num1, num2):
    if '.' in num1 and num1.replace('.', '').isdigit():
        num1 = float(num1)
    elif num1.isdigit():
        num1 = int(num1)

    if '.' in num2 and num2.replace('.', '').isdigit():
        num2 = float(num2)
    elif num2.isdigit():
        num2 = int(num2)

    # делим в блоке попытка исключение - вдруг там ноль
    res = None
    try:
        res = num1 / num2
    except ZeroDivisionError:
        # Если при делении возникла ошибка - результат ставим неопределено
        print('incorrent arguments')
    finally:
        # возвращаем результат в точку вызова
        return res


# выводим результат
result = mydevide(input('N1:'), input('N2:'))
print(result)
