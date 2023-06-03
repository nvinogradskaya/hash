import collections

def main():
    given_numbers = []
    salted_numbers = []
    salt = []
    with open("given_numbers.rtf", "r") as given_number:
        for num in given_number:
            given_numbers.append(int(num))

    with open("salted_numbers.rtf", "r") as salted_number:
        for num in salted_number:
            salted_numbers.append(int(num))

    for salted_number in salted_numbers:
        for given_number in given_numbers:
            salt.append(salted_number - given_number)

    print([number for number, n in collections.Counter(salt).items() if n == 5])


if __name__ == "__main__":
    main()