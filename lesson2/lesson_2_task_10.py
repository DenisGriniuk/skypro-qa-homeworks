def bank(X, Y):
    сумма = X * (1 + 0.1) ** Y
    return сумма

X = float(input("Введите размер вклада: "))
Y = int(input("Введите срок вклада в годах: "))

итоговая_сумма = bank(X, Y)
print("Итоговая сумма на счету после", Y, "лет:", итоговая_сумма)
