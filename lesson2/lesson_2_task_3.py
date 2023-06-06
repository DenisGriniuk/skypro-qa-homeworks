import math

def square(side):
    area = side * side
    if not isinstance(area, int):
        area = math.ceil(area)
    return area

side_str = input("Введите сторону квадрата: ")
side_str = side_str.replace(',', '.') 
side = float(side_str)
area = square(side)
print(area)
