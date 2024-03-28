numbers = [7, 14, 16, 18, 40]
user_number = int(input("Введите число: "))
if user_number in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")
print("Исходный список:", numbers)
print("Число пользователя:", user_number)