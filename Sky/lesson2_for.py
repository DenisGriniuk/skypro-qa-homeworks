for x in range(1, 21):
   print("x=", x, "x2=", x*x)
    
students = ["Алексей", "Мизаил", "Денис", "Александра", "Маргарита", "Олеся", "Виктор"]

l = len(students)

for i in range(0,l):
    print(students[i])

# слово 
word = "Test"

for s in word:
    print(s)



for student in students:
    print(student)

# напечатать только нечётные числа
nums = [1,2,3,4,5,6,7,8,9,10]

for n in nums:
    if (n % 2 == 1):
        print(n)


