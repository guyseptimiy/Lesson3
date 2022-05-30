# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def mycapitalize(string):
    return string.capitalize()


my_string = " ".join([mycapitalize(el) for el in input('string to proceed:').split()])

print(my_string)
