from user import User
from card import Card

alex = User("Alex")
# denis = User("Denis")
# marta = User("Marta")

alex.sayName()
alex. setAge(21)
alex.sayAge()

card = Card("3334 4678 8765 9999", "11/28", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)
