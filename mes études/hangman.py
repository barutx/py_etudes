# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "/Users/barut/Desktop/computation/mit6_.0001/psMITxCS/ps2/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word: 
        if i in letters_guessed: 
            pass
        else:
            return False 
    return True

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    for i in secret_word:
      if i not in letters_guessed:
          secret_word = secret_word.replace(i,"_ ")
    return secret_word
    
  
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

def number_guess(secret_word,letter,num_guess):
    """secret_word: string, the word the user is guessing
    letter: a single letter the user inserts as input
    num_guess: total number of guesses in the game
    returns: the number of remaining guesses after each input"""
    vowel=["a","e","o","i","u"]
    if letter in secret_word:
        return num_guess
    elif letter not in secret_word:
        if letter in vowel:
            if num_guess >= 2:
                num_guess -= 2
            else: 
                num_guess -= 1           
        else:
            num_guess -= 1
    return num_guess
        
def total_guess_calcul(num_guess, secret_word):
    letters_secret_word = list(secret_word)
    for i in letters_secret_word:
        if letters_secret_word.count(i)>1:
            k = letters_secret_word.index(i)
            del letters_secret_word[k]
        else:
            pass    
    total_score = num_guess * len(letters_secret_word)
    return print(f"Your total score is: {total_score}")       
    

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    remained_letters = string.ascii_lowercase
    for i in remained_letters:
        if i in letters_guessed:
            remained_letters = remained_letters.replace(i,"")
    return remained_letters

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    
def get_letter():
    """Ask for a letter to guess to the user, assumes that input is alphabet and in lowercase 
    returns: string, if input meets conditions."""    
    
    letter_guessed = input("Make your guess: ")       
    if len(letter_guessed) == 1 and letter_guessed.isalpha() or letter_guessed =="*":     
        return letter_guessed
    else:
        return False



    
####### HANGMAN WITHOUT HINTS ############
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed=[]
    print("Welcome to the game Hangman !")
    print(f"I am thinking of a word that is {len(secret_word)} letters long. ")
    num_guess = 9
    num_warn = 3
    print("------------------------")
    print(f"You have {num_guess} guesses left.")
    print("Available letters: ", get_available_letters(letters_guessed)) 
    available_letters = list(get_available_letters(letters_guessed))   
    while True:
        if num_guess <= 0: 
            print("Haha...Ψ(｀∀ ´#)ﾉ you've lost. Secret word was: ", f"{secret_word}")
            break
        letter = get_letter()
        if letter is not False and num_guess > 0:
            letters_guessed.append(letter)
            if is_word_guessed(secret_word,letters_guessed):
                print("Congratulations, you've won ╰(°ㅂ°)╯! Secret word was: ", secret_word)
                break
            elif letter not in available_letters:
                num_guess -= 1
                print("OOps, you've already used that letter ( •̀ᴗ•́ )و ̑̑.")                
            elif letter in secret_word:
                num_guess = number_guess(secret_word,letter,num_guess)
                print("Good guess: ", get_guessed_word(secret_word,letters_guessed))
            else:
                num_guess = number_guess(secret_word,letter,num_guess)
                print("OOps That letter is not in my word ( •̀ᴗ•́ )و ̑̑.: ", get_guessed_word(secret_word,letters_guessed))
            available_letters = list(get_available_letters(letters_guessed))
            print("------------------------")
            print(f"You have {num_guess} guesses left.")
            print("Available letters: ", get_available_letters(letters_guessed))
            

        elif letter is False:
            num_warn -=1
            print(f"Invalid input. You have {num_warn} warning left. Please enter a single letter. ")
            print(get_guessed_word(secret_word, letters_guessed))
            if num_warn == 0:
                num_guess -= 1
                print("You have lost 1 guess")
                num_warn = 3
            else: 
                continue
    total_guess_calcul(num_guess,secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------




def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    my_word = get_guessed_word(secret_word,letters_guessed)
    k = 0
    my_word = my_word.replace(" ","")
    other_word = other_word.replace(" ","")
    for i in my_word:
        j = my_word.index(i,k)   #### k variable ensures no precedent appearance of a letter taken as index
        k +=1
        if i.isalpha():                #### THIS PART IS TO ENSURE THAT THERE IS NO MATCHES LIKE "A_PLE == "APPLE"
            if i == other_word[j] and my_word.count(i) == other_word.count(i):         
                pass
            else:
                return False
        elif i == "_" and len(my_word) == len(other_word):
            pass
        else:
            return False
    return True





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''   
    my_word = get_guessed_word(secret_word, letters_guessed)
    k = 0
    my_word = my_word.replace(" ","")
    print("Hints are here ╰(°ㅂ°)╯ : ")

    for word in wordlist:
        if match_with_gaps(my_word,word):
            print(word, end=" ")
        else:
            pass
    print("\n")   





def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global letters_guessed
    letters_guessed = []
    print("Welcome to the game Hangman !")
    print(f"I am thinking of a word that is {len(secret_word)} letters long. ")
    num_guess = 6
    num_warn = 3
    print("------------------------")
    print(f"You have {num_guess} guesses left.")
    print("Available letters: ", get_available_letters(letters_guessed)) 
    available_letters = list(get_available_letters(letters_guessed))   
    while True:
        if num_guess <= 0: 
            print("Haha...Ψ(｀∀ ´#)ﾉ you've lost. Secret word was: ", f"{secret_word}")
            break
        letter = get_letter()
        if letter is not False and num_guess > 0:
            letters_guessed.append(letter)
            if is_word_guessed(secret_word,letters_guessed):
                print("Congratulations, you've won ✧⋆٩(ˊᗜˋ )و ♡✧! Secret word was: ", secret_word)
                break
            elif letter == "*":
                show_possible_matches(secret_word)
            elif letter not in available_letters:
                num_guess -= 1
                print("OOps, you've already used that letter ( •̀ᴗ•́ )و ̑̑.")                
            elif letter in secret_word:
                num_guess = number_guess(secret_word,letter,num_guess)
                print("Good guess: ", get_guessed_word(secret_word,letters_guessed))
            else:
                num_guess = number_guess(secret_word,letter,num_guess)
                print("OOps That letter is not in my word ( •̀ᴗ•́ )و ̑̑.: ", get_guessed_word(secret_word,letters_guessed))
            available_letters = list(get_available_letters(letters_guessed))
            print("------------------------")
            print(f"You have {num_guess} guesses left.")
            print("Available letters: ", get_available_letters(letters_guessed))
            



        elif letter is False:
            num_warn -=1
            print(f"Invalid input. You have {num_warn} warning left. Please enter a single letter. ")
            print(get_guessed_word(secret_word, letters_guessed))
            if num_warn == 0:
                num_guess -= 1
                print("You have lost 1 guess")
                num_warn = 3
            else: 
                continue
    total_guess_calcul(num_guess,secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
