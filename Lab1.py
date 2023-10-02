def task1():
    s = inputInt("Введите количество секунд: ")

    days = int(s / (24 * 60 * 60))
    hours = int((s % (24 * 60 * 60)) / (60 * 60))
    minutes = int((s % (60 * 60)) / 60)
    seconds = s % 60

    print("Результат: ", days, ":", hours, ":", minutes, ":", seconds, sep="")


def task2():
    str = input("Введите строку: ")

    print("Значения Unicode:")
    for ch in str:
        print(ord(ch), end=" ")

    print("")

    words = str.split(' ')

    maxWord = ""
    max = 0
    for word in words:
        if len(word) > max:
            max = len(word)
            maxWord = word

    print("Самое длинное слово:", maxWord)


def task3():
    n = inputInt("Введите n: ")

    numbers = []
    for i in range(n):
        numbers.append(inputInt("Введите " + str(i + 1) + "-е число: ") ** 3)

    print("Список кубов:")
    print(numbers)

    sum = 0
    mult = 1
    for number in numbers:
        sum += number
        mult *= number

    print("Сумма =", sum)
    print("Произведение =", mult)

    print("Обратный список: ")
    for i in range(len(numbers) - 1, -1, -1):
        print(numbers[i], end=" ")

    print("")


def task4():
    my_dict = dict([('a', 500), ('b', 5874), ('c', 560), ('d', 400), ('f', 20)])
    print("Словарь: ")
    print(my_dict)

    items_list = list(my_dict.items())

    for i in range(len(items_list)):
        for j in range(i + 1, len(items_list)):
            if items_list[j][1] > items_list[i][1]:
                temp = items_list[j]
                items_list[j] = items_list[i]
                items_list[i] = temp

    print("Ключи с максимальными значениями:")
    for i in range(3):
        print(items_list[i][0], "-", items_list[i][1])


def task5():
    shop_items = {"Колье": [10, "Золото, бриллиант", 10000],
                  "Кольцо": [5, "Серебро", 15000],
                  "Серьги": [14, "Золото, топазы высокого качества", 3000]}

    isWork = True
    while isWork:
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Просмотр всей информации")
        print("5. Покупка")
        print("6. Выход")

        match (inputInt("Выберите вариант: ")):
            case 1:
                for key in shop_items:
                    print(key, "-", shop_items.get(key)[1])
            case 2:
                for key in shop_items:
                    print(key, "-", shop_items.get(key)[2])
            case 3:
                for key in shop_items:
                    print(key, "-", shop_items.get(key)[0])
            case 4:
                for key in shop_items:
                    print(key, ":", sep="")
                    print("Описание:", shop_items.get(key)[1])
                    print("Количество:", shop_items.get(key)[2])
                    print("Цена:", shop_items.get(key)[0])
            case 5:
                name = input("Введите название: ")

                isNeedToDelete = False
                keyToDelete = ""

                isFound = False
                for key in shop_items:
                    if key == name:
                        isFound = True

                        count = inputInt("Введите количество: ")
                        if (count > shop_items.get(key)[0]):
                            print("В магазине нет столько товара!")
                        else:
                            print("Куплено товаров на сумму", shop_items.get(key)[2] * count, "руб.")

                            shop_items.get(key)[0] -= count
                            print(shop_items.get(key)[0], "осталось")
                            if shop_items.get(key)[0] == 0:
                                isNeedToDelete = True
                                keyToDelete = key

                if not isFound:
                    print("Товар не найден!")

                if isNeedToDelete:
                    shop_items.pop(keyToDelete)
            case 6:
                isWork = False
            case _:
                print("Некорректный ввод!")


def task6():
    numbers = input("Введите числа через запятую: ")

    subnumbers = numbers.split(",")

    numbers = []

    isOnlyNumbers = True
    for subnumber in subnumbers:
        subnumber = subnumber.replace(' ', '')
        subnumber = subnumber.replace(',', '')

        if subnumber.isdigit():
            numbers.append(int(subnumber))
        else:
            isOnlyNumbers = False
            break

    if not isOnlyNumbers:
        print("Некорректный ввод")
    else:
        print("Список:", numbers)
        print("Кортеж", tuple(numbers))


def inputInt(description):
    str = input(description)
    while not str.isdigit():
        print("Некорректный ввод")
        str = input()

    return int(str)


def main():
    isWork = True

    while isWork:
        print("1. Задача 1")
        print("2. Задача 2")
        print("3. Задача 3")
        print("4. Задача 4")
        print("5. Задача 5")
        print("6. Задача 6")
        print("7. Выход")

        match (inputInt("Выберите вариант: ")):
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 4:
                task4()
            case 5:
                task5()
            case 6:
                task6()
            case 7:
                isWork = False
            case _:
                print("Некорректный ввод")


main()

