
# HangMan.
import random
from Words import Words
import string
import emoji

def Hangman():
    word = get_valid_word(Words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    print()
    print("Hey Scholar! Let's play")
    print()
    Lives = 7
    
    while len(word_letter) > 0 and Lives > 0:
        print("Lives:",Lives)
        print("Word used: ", " ".join(used_letters)) 
        word_segment = list()
        for letter in word.upper():
           if letter in used_letters:
            word_segment += letter
           else: word_segment += "_"   
        print("Current Word ", " ".join(word_segment))
       
        user_input = input("Letter suitable: " ).strip().upper()
           
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
            else: 
               Lives = Lives - 1
               print("Letter not in Word")
        else:
            print("Invalid input")
    if Lives == 0:
       print("\nSORRY the Word's", word)
    else:
       pri = emoji.emojize(":thumbs_up:")
       print("Congratulation Scholar!\n" 
             "you guessed The Word", pri, word.upper())
    
def get_valid_word(word):
   word = random.choice(Words)
   while "-" in word:
    word = random.choice(Words)
   return word.upper()

Hangman()
      



