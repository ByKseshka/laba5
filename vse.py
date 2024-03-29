def zad1():
    numbers = [7, 14, 16, 18, 40]
    user_number = int(input("Введите число: "))
    if user_number in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
    print("Исходный список:", numbers)
    print("Число пользователя:", user_number)

def zad2():
    list = [1, 5, 2, 3, 1, 4, 2, 5]
    povtor = set()
    for num in list:
        if list.count(num) > 1:
            povtor.add(num)
    if povtor:
        print("Повторяющиеся элементы в списке:", povtor)
    else:
        print("В списке нет повторяющихся элементов.")

def zad3():
    days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    num_weekends = int(input("Сколько выходных дней на неделе вы хотите? "))

    weekends = days_of_week[-num_weekends:]
    workdays = days_of_week[:len(days_of_week) - num_weekends]

    if 0 < num_weekends <= len(days_of_week):
        weekends = days_of_week[-num_weekends:]
        workdays = days_of_week[:-num_weekends]
        print("Ваши выходные дни:", ", ".join(weekends))
        print("Ваши рабочие дни:", ", ".join(workdays))
    else:
        print("Некорректный ввод. Количество выходных дней должно быть в диапазоне от 1 до", len(days_of_week))

def zad4():
    group1 = ['Полякова', 'Криштал', 'Пономаренко', 'Куклина', 'Гилязова', 'Епифанова', 'Латышева', 'Свечкова',
              'Королева', 'Федоров']
    group2 = ['Балабан', 'Паймина', 'Денисова', 'Лисицына', 'Ескина', 'Алиева', 'Ахмедова', 'Коробова', 'Золова',
              'Добродеева']

    team = tuple(group1[:5] + group2[:5])

    print("Группа 1:", group1)
    print("Группа 2:", group2)
    print("Спортивная команда:", team)

    print("Длина кортежа:", len(team))

    sorted_team = sorted(team)
    print("Отсортированная команда:", sorted_team)

    student = "Иванов"
    if student in team:
        count = team.count(student)
        print(f"Студент {student} входит в команду. Его фамилия встречается {count} раз(а).")
    else:
        print(f"Студент {student} не входит в команду.")