while True:
    chislo1 = int(input("Введите первое число: "))
    chislo2 = int(input("Введите второе число: "))
    rez = input("введите символ: ")
    if rez == "+":
        print("результат операции = ", chislo1 + chislo2)
    if rez == "-":
        print("результат операции = ", chislo1 - chislo2)
    if rez == "/":
        print("результат операции = ", chislo1 / chislo2)
    if rez == "*":
        print("результат операции = ", chislo1 * chislo2)
    if "y" == input("завершить? введите y: "):
        break 