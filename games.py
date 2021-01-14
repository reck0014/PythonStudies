import guessing
import hangman

print("*****************************")
print("******Choose your game!******")
print("*****************************")

game = int(input("Hit (1) for Guessing and (2) for Hangman:"))

if game == 1:
    print("Playing Guessing")
    guessing.play_guessing()
elif game == 2:
    print("Playing Hangman")
    hangman.play_hangman()

