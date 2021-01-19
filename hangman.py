import random


def play_hangman():
    print_open_message()
    secret_word = load_secret_word()
    correct_letters = start_correct_letters(secret_word)
    print(correct_letters)

    hanged = False
    guessed = False
    errors = 0

    # game loop
    while not hanged and not guessed:

        guess = enter_guess()

        if guess in secret_word:
            check_correct_guess(guess, correct_letters, secret_word)
        else:
            errors += 1
            draw_hang(errors)
            print("Error. You still have {} chances".format(6 - errors))

        hanged = errors == 7
        guessed = "_" not in correct_letters

        print(correct_letters)

    if guessed:
        print_winner_message()
    else:
        print_loser_message(secret_word)


def print_open_message():
    print("****************************")
    print("Welcome to the hangman game!")
    print("****************************")


def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))

    secret_word = words[number].upper()

    return secret_word


def start_correct_letters(word):
    return ["_" for letter in word]


def enter_guess():
    guess = input("Which letter?").strip().upper()
    return guess


def check_correct_guess(guess, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if guess == letter:
            correct_letters[index] = letter
        index += 1


def print_winner_message():
    print("You Win!!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loser_message(secret_word):
    print("Loser!!!!")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def draw_hang(errors):
    print("  _______     ")
    print(" |/      |    ")

    if (errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play_hangman()
