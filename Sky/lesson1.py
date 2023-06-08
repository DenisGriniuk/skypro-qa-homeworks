# name = "Денис"

# print("Привет, " + name + "!")
# print("Как прошёл твой день, " + name + "?")
# print("Что ты сегодня ел, " + name + "?")

#weekDays = ["Понедельник", "Вторинк", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

#lenght = len(weekDays)
#print(lenght)

#monday = weekDays[0]
#print(monday) 

#def sum_numbers():    
 #   print("меня вызвали 1")
 #   print("меня вызвали 2")
 #   print("меня вызвали 3")
 #   print("меня вызвали 4")

#sum_numbers()

#def greet(name):
 #   print("Привет, " + name)

#greet("Denis")
#greet("Margarita")

def sum_numbers(num_1, num_2):
    print("Слагаемое 1 = ", num_1)
    print("Слагаемое 2 = ", num_2)
    result = num_1+num_2
    print("Сумма = ", result)
    return result

def multiply(x,y):
    return x*y

x = sum_numbers(4,5)
print(x)

m = multiply(3,4)
print(m)