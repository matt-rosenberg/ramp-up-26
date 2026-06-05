def possible_eats(n):
    area = n * n
    return area.bit_length() - 1

def main():
    print(possible_eats(6))

if __name__ == "__main__":
    main()