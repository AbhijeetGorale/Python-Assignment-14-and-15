from functools import reduce

minimum = lambda numbers: reduce(lambda a, b: a if a < b else b, numbers)


def main():

     Data = [11,10,15,20,22,27,30,36]
     print("Minimum number is:", minimum(Data))


if __name__ == "__main__":
    main()