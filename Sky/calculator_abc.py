from lesson4_calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0


# ++
# - -
# - +
# . .
# n 0

# print("start")
# res = calculator.sum(4, 5)
# assert res == 9

# res = calculator.sum(-6, -10)
# assert res == -16

# res = calculator.sum(-6, 6)
# assert res == 0

# # doubt result?
# res = calculator.sum(5.6, 4.3)
# res = round(res, 1)
# print(res)
# assert res == 9.9

# res = calculator.sum(10, 0)
# assert res == 10

# res = calculator.div(10, 2)
# assert res == 5

# numbers = [1,2,3,4,5,6,7,8,9,5]
# res = calculator.avg(numbers)
# print(res)
# assert res == 5

# print("finish")

# res = calculator.div(10, 0)
# assert res == None

