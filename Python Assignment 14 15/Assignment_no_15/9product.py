from functools import reduce

def main():
    product = lambda numbers: reduce(lambda a, b: a * b, numbers)

    Data = [1,2,3,4,5,6]

    print("Product of all elements is:", product(Data))

if __name__=="__main__":
    main()
