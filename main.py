import random


def get_inputs_from_user():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    return nr_letters, nr_symbols, nr_numbers


def generate_password(policy):

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password = ""

    len_letters = len(letters)
    len_numbers = len(numbers)
    len_symbols = len(symbols)

    for _ in range(policy[0]):
        password += letters[random.randint(0, len_letters - 1)]

    for _ in range(policy[1]):
        password += symbols[random.randint(0, len_symbols - 1)]

    for _ in range(policy[2]):
        password += numbers[random.randint(0, len_numbers - 1)]

    return "".join(random.sample(password, len(password)))


if __name__ == "__main__":

    print(generate_password(get_inputs_from_user()))
