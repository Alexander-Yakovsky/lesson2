"""Выбрать минимум 5 известных людей и узнать их год рождения. Программа должна по очереди спрашивать
у пользователя год рождения знаменитости. После того как пользователь ввел все ответы, программа считает
и выводит на экран:
- количество правильных ответов
- количество ошибок
- процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
- процент неправильных ответов
После вывода информации программа спрашивает
пользователя хочет ли он начать игру сначала, если да - то повторяем все сначала, если ответ нет - выходим из программы
- В программе с помощью комментариев написать подсказки - правильные ответы для каждой знаменитости"""

"""Путин 1952
Пушкин 1799
Ленин 1870
Сталин 1878
Черчиль 1874"""



correct_answer = 0 #Правильные ответы
bad_answer = 0 #Неправильные ответы

while True:
    date_year = int(input("Введите год роджения А.С Пушкина:")) #1799
    if date_year == 1799:
        correct_answer += 1
        print("Отлично ты угадал")
    else:
        bad_answer += 1
        print("Ты не угадал")

    date_year = int(input("Введите год роджения Черчиля:")) #1874
    if date_year == 1874:
        correct_answer += 1
        print("Отлично ты угадал")
    else:
        bad_answer += 1
        print("Ты не угадал")

    date_year = int(input("Введите год роджения Ленина:")) #1870
    if date_year == 1870:
        correct_answer += 1
        print("Отлично ты угадал")
    else:
        bad_answer += 1
        print("Ты не угадал")

    date_year = int(input("Введите год роджения Путина:")) #1952
    if date_year == 1952:
        correct_answer += 1
        print("Отлично ты угадал")
    else:
        bad_answer += 1
        print("Ты не угадал")

    date_year = int(input("Введите год роджения Сталина:"))  #1878
    if date_year == 1878:
        correct_answer += 1
        print("Отлично ты угадал")
    else:
        bad_answer += 1
        print("Ты не угадал")

    percent_correct_answer = int(correct_answer * 100 / (correct_answer + bad_answer))  # Процент правильных ответов
    percent_bad_answer = int(bad_answer * 100 / (correct_answer + bad_answer))  # Процент неправильных ответов

    print("Процент правильных ответов: ", percent_correct_answer, "%")
    print("Процент не правильных ответов: ", percent_bad_answer, "%")

    restart = input("Сыграм еще? (да/нет):")
    if restart == ("да"):
        print("Отлично, поехали заново!!!")
    else:
        break

print("END")