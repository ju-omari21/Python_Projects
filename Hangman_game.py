import random
my_list_words = ["PHP", "Python", "JavaScript", "Java", "HTML","React"]
rand_word = random.choice(my_list_words)
your_guess = []

tries = 6
"""Create a variable called stored_word to store the word with underscores for
 each letter that has not been guessed"""
stored_word = "_" * len(rand_word)
print("Heyy There, Welcome to Hangman Game, Hope You Enjoy it!")
print(stored_word)

while tries > 0 and stored_word != rand_word:
  guess = input("Guess a letter: ").lower()

  if guess in your_guess:
    print("You have already guessed that letter.")
  elif guess in rand_word:
    print("Cherries, you guessed a correct letter.")

    your_guess.append(guess)
    stored_word = "".join([letter if letter in your_guess else "_" for letter in rand_word])
    print(stored_word)

  else:
    print("Opppsss, You guessed a wrong letter.")

    tries -= 1
    print(f"You have {tries} tries left.")

if stored_word == rand_word:
  print("Great dud, You have won!")
else:
  print(f"You have lost. The word was {rand_word}.")
