# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# начальная сумма равна нулю
summa = 0

# Организцем бесконечный цикл
while 1 == 1:
    # просим пользователя вводить числа или х для выхода
    spisok = input('enter numbers or x for exit:').split()

    # суммируем все элементы в списке которые представляют собой число
    for el in spisok:
        if el.isdigit():
            summa += int(el)
    # выводим сумму числе
    print(summa)

    # Если в списке есть Х - прекращаем ввод
    if 'x' in spisok:
        break
