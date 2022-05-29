#  Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
#  имя, фамилия, год рождения, город проживания, email, телефон.
#  Функция должна принимать параметры как именованные аргументы.
#  Осуществить вывод данных о пользователе одной строкой.

# Описываем функцию выода данных пользователя одной строкой
def get_user_info(lname, fname, year, town, mail, phonenum):
    print(
        f'last_name: {lname}, first_name: {fname}, birth year: {year}, city: {town}, email: {mail}, phone: {phonenum}')


# вводим данные пользователя одной строкой
last_name, first_name, year_of_birth, city, email, phone = input(
    'last_name first_name year_of_birth city, email phone:').split()

# осуществляем вызов функции
get_user_info(last_name, first_name, year_of_birth, city, email, phone)
