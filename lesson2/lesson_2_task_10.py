def bank(deposit_amount, years):
    sum = deposit_amount * (1 + 0.1) ** years
    return sum

deposit_amount = float(input("Введите размер вклада: "))
years = int(input("Введите срок вклада в годах: "))

total_sum = bank(deposit_amount, years)
print("Итоговая сумма на счету после", years, "лет:", total_sum)
