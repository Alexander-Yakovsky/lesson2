try_negative = "Не правильно, еще попытка"
try_positive = "Супер, все верно!!"

while True:
    date_year = int(input("Введите год роджения А.С Пушкина:"))
    if date_year == 1799:
        break
    print(try_negative)
print(try_positive , "А теперь давай угадаем какой день. Подсказка он родился в Июне ;)")

#Проверка дня рождения
while True:
    date_day = int(input("Введите день роджения А.С Пушкина:"))
    if date_day == 6:
        break
    print(try_negative)
print(try_positive)

print("END")