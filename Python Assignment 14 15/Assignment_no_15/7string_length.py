
city = lambda strings: list(filter(lambda s: len(s) > 5, strings))

def main():

    Data = ["abhi", "chennai", "pune", "mumbai", "example", "enjoy", "marvellous","infosystem"]
    print("Filtered list:", city(Data))


if __name__ == "__main__":
    main()
