secret = "yo"
guess = ""
limit = 3

while limit > 0:
    guess = input("Enter word: ")
    if(guess == secret):
        break
    limit -= 1

if(limit == 0):
    print("Out of guesses!")
else:
    print("Correct!")