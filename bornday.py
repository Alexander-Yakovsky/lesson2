"""9. Написать программу или модернизировать предыдущую используя условные операторы:
- Спросить у пользователя год рождения А.С. Пушкина
- Если пользователь ввел верный год спросить у него день рождения
- Если день рождения введен верно вывести 'Верно'
- Если день рождения введен неверно вывести 'Неверный день рождения'
- Если неверно введен год, то сразу вывести 'Неверный год"""

date_year = int(input("Введите год роджения А.С Пушкина:"))
if date_year == 1799:
    print("Верно")
    date_day = int(input("Введите день роджения А.С Пушкина:"))
    if date_day == 6:
        print("Верный день")
    else:
        print("Неверный день, досвидания")
else:
    print("Неверный год, даже день спрашивать не буду")

