divisible= lambda numbers: list(filter(lambda n: n % 3 == 0 and n % 5 == 0, numbers))

def main():
    Data = [10,11,15,27,30,35,41,45,50]
    print("divisible no are:", divisible(Data))

if __name__=="__main__":
    main()    