import random, os, sys



fruits = ["apple", "apricot", "avocado", "banana", "blackberry","blueberry", "cantaloupe", "cherry", "coconut", "cranberry","date", "fig", "grape", "grapefruit", "guava","honeydew", "kiwi", "lemon", "lime", "mango","nectarine", "orange", "papaya", "peach", "pear","pineapple", "plum", "pomegranate", "raspberry","strawberry", "tangerine", "watermelon"]
already_guessed = []
found_letters_index = []
constructed_word = []
lives = 6

def pick_random_word():
    random_number = random.randint(0, len(fruits)-1)
    random_word = fruits[random_number]
    return random_word

def guess_a_letter(random_word):
        # ask user for a letter
        guess = input('Guess a letter (enter "1" to reset game, "2" to exit)')
        # check to make sure they only enter 1 character
        if len(guess) != 1:
            print("you can only guess 1 letter")
            return
        #check for "1" which means to restart game
        if guess == "1":
            reset_game()
            return
        #check for a "2" which means to exit
        if guess == "2":    
            os.system('cls')
            print("Goodbye!")
            sys.exit()


        #check for a letter that was already guessed
        for letter in already_guessed:
            if guess == letter:
                print("You already guessed that letter")
                return
        #add guessed letter to already guessed
        already_guessed.append(guess)

        #check to see if they got any letters correct
        check_letter(guess, random_word)

       

def check_letter(guess, random_word):
    global lives
    hits_this_turn = False
    found_index = 0
    for letter in random_word:
        if letter == guess:
            found_letters_index.append(found_index)
            hits_this_turn = True
        found_index += 1
    print("=======================================")
    print("=======================================")
    if hits_this_turn:
        print (F'"{guess}" is in the word!')
    else:
        print (F'"{guess}" is not in the word. You lost a life!')
        lives -= 1

    display_results()
#function to construct the word to show the user what it looks like with correct guesses and blanks
def construct_word(random_word):
    constructed_word.clear()
    for i in range(len(random_word)):
        if i in found_letters_index:
            constructed_word.append(random_word[i])
        else:
            constructed_word.append("_")

def display_results():
    if lives < 1:
        print("You Lose!!!")
        print("The word was: " + "".join(random_word))
        return
    if len(found_letters_index) == len(random_word):
        print("YOU WIN!!!!")
        print("The word was: " + "".join(random_word))
    else:
        construct_word(random_word)
        print(f"Lives remaining: {lives}")
        print(" ".join(constructed_word))
        print("Guessed letters: " + ", ".join(sorted(already_guessed)))
    print("=======================================")
    print("=======================================")


def reset_game():
    global lives
    already_guessed.clear()
    found_letters_index.clear()
    constructed_word.clear()
    lives = 6
    print("GAME WAS RESET")
    print("=====================")
    return pick_random_word()

# start the game by picking a random word
random_word = pick_random_word()
print(" ".join("_" for letter in random_word))


# while the user has lives and the word hasn't been found already, run a loop to allow guesses
while lives > 0  and len(found_letters_index) != len(random_word):
    guess_a_letter(random_word)

