import random

people = {
    'Иван': '02.01.1988',
    'Мария': '15.05.1992',
    'Алексей': '10.11.1985',
    'Елена': '25.07.1990',
    'Андрей': '12.03.1995',
    'Ольга': '08.09.1982',
    'Дмитрий': '30.04.1998',
    'Наталья': '18.12.1989',
    'Сергей': '06.06.1993',
    'Анна': '22.08.1996'
}

while True:
    # Выбираем 5 случайных людей
    random_people = random.sample(list(people.keys()), 5)

    correct_answers = 0
    wrong_answers = 0

    for person in random_people:
        # Выводим имя человека и запрашиваем дату рождения
        date = input(f"Введите дату рождения для {person}: ")

        # Проверяем правильность ответа
        if date == people[person]:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неправильно. Правильный ответ: {person} родился {people[person]}")
            wrong_answers += 1

    # Выводим результаты
    print(f"Правильных ответов: {correct_answers}")
    print(f"Неправильных ответов: {wrong_answers}")

    # Предлагаем начать снова
    play_again = input("Хотите начать снова? (да/нет): ")
    if play_again.lower() != "да":
        break
