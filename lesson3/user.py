class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirstName(self):
        print("Моё имя", self.first_name)

    def sayLastName(self):
        print("Моя фамилия", self.last_name)

    def sayFullName(self):
        print("Меня зовут", self.first_name + ' ' + self.last_name)

user = User("Denis", "Griniuk")
user.sayFirstName()  
user.sayLastName()   
user.sayFullName()   

