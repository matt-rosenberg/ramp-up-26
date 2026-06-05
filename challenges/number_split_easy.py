def number_split(num):
    a = num // 2
    b = num - a
    return a,b

def main():
    print(number_split(17))

if __name__ == "__main__":
    main()