even = lambda numbers: len(list(filter(lambda n: n % 2 == 0, numbers)))

def  main():
    Data = [11, 10, 15, 20, 22, 27, 30]
    print("Count of even no:",even(Data))


if __name__=="__main__":
    main()