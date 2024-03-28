days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
num_weekends = int(input("Сколько выходных дней на неделе вы хотите? "))

weekends = days_of_week[-num_weekends:]
workdays = days_of_week[:len(days_of_week)-num_weekends]

if 0 < num_weekends <= len(days_of_week):
    weekends = days_of_week[-num_weekends:]
    workdays = days_of_week[:-num_weekends]
    print("Ваши выходные дни:", ", ".join(weekends))
    print("Ваши рабочие дни:", ", ".join(workdays))
else:
    print("Некорректный ввод. Количество выходных дней должно быть в диапазоне от 1 до", len(days_of_week))
