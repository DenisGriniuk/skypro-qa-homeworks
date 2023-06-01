# Високосный год

def is_year_leap(year):
  if year % 4 != 0:
    print(f'Год {year}: False')
  else:
    print(f'Год {year}: True')
year = int(input('Введите год: '))
is_year_leap(year)
