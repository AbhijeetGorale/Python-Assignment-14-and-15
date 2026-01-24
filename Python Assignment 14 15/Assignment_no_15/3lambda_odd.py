Checkodd = lambda No: (No % 2 == 1)

def main():
    Data = [6, 9, 11, 10, 15, 20, 22, 27, 30, 31, 41, 42]
    Filt = list(filter(Checkodd, Data))
    print("Data after filter is:", Filt)

if __name__ == "__main__":
    main()