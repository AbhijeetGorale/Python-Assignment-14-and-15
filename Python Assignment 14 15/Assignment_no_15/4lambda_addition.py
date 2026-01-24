from functools import reduce

addition = lambda numbers: reduce(lambda a, b: a + b, numbers)

Data = [1,1,5,2,2,2,3,9]

print("Addition of all numbers is:", addition(Data))