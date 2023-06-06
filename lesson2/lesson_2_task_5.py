def season_month(month):
    if month in (1, 2, 12):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Некорректный номер месяца"

month = int(input("Введите номер месяца (от 1 до 12): "))
season = season_month(month)
print(season_month(month))
