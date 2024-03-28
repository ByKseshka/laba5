list = [1,5,2,3,1,4,2,5]
povtor = set()
for num in list:
    if list.count(num) > 1:
        povtor.add(num)
if povtor:
    print("Повторяющиеся элементы в списке:", povtor)
else:
    print("В списке нет повторяющихся элементов.")