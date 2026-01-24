
largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

def main():

   print(largest(10, 25, 15))    


if __name__=="__main__":
    main()