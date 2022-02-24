import random

def hangman():
    "This function runs the game hangman.."
    word_list = ['various', 'random', 'words', 'to', 'choose', 'from']
    game_word = random.choice(word_list)
    word1 = list(game_word)
    guess = (len(game_word) * '-')
    guess_list = list(guess)
    letters_not = []
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    p8 = '''
    '''
    p7 = '''   
          
          
          
         
    _________'''
    p6 = '''   
       |   
       |   
       |   
       |  
    ___|_____'''
    p5 = '''       ____
       |   
       |   
       |   
       |  
    ___|_____'''
    p4 = '''       ____
       |   |
       |   
       |   
       |  
    ___|_____'''
    p3 = '''       ____
       |   |
       |   O
       |   
       |  
    ___|_____'''
    p2 = '''       ____
       |   |
       |   O
       |   |
       |  
    ___|_____'''
    p1 = '''       ____
       |   |
       |  \O/
       |   |
       |  
    ___|_____'''
    p0 = '''       ____
       |   |
       |  \O/
       |   |
       |  / \\
    ___|_____'''
    pic = [p0, p1, p2, p3, p4, p5, p6, p7, p8]
    print(f"\n{guess}")

    t = 8
    while t > 0:
        letter = input("Input a letter:")
        if len(letter) != 1:
            print("You should input a single letter")
            print("\n" + ("".join(guess_list)))
            print(pic[t])
        elif letter not in lowercase:
            print("Please enter a lowercase English letter")
            print("\n" + ("".join(guess_list)))
            print(pic[t])
        elif letter in guess_list or letter in letters_not:
            print("You've already guessed this letter")
            print("\n" + ("".join(guess_list)))
            print(pic[t])
        elif letter not in word1:
            print("That letter doesn't appear in the word")
            letters_not.append(letter)
            if t > 1:
                print("\n" + ("".join(guess_list)))
            elif t == 1:
                print("You lost!\n")
                t = t - 1
                print(pic[t])
                break
            t = t - 1
            print(pic[t])
        elif letter in word1:
            for i in range(0, len(word1)):
                if letter == word1[i]:
                    guess_list[i] = letter
                    guess_update = "".join(guess_list)
            print("\n" + "".join(guess_list))
            print(pic[t])
            if "".join(guess_list) == game_word:
                print(f"You guessed the word {game_word}!\nYou survived!\n")
                break
            else:
                continue
    return

def play_or_exit():
    "Asks player if he wants to play the game or exit"
    play_exit = input('Type to "play" to play the game, "exit" to quit:')
    if play_exit == "play":
        hangman()
        play_or_exit()
    else:
        exit()
    return

print('H A N G M A N')
play_or_exit()
