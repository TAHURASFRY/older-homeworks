import random
import turtle

score = 6
True_chars = []
words = ['tree', 'shadow', 'xeus', 'college', 'happy', 'vanilla', 'tobacco', 'elephant', 'lion', 'planet']
word = random.choice(words)



while True:
    for i in range(len(word)): 
        if word[i] in True_chars:
         print(word[i], end='')
        else:
         print(' _ ', end= '')
    print("\npls enter a character")
    char = input( )

    if char in word:
        True_chars.append(char)
    else:
        score -= 1
        print("wrong character")
        print(score)
    
    if score == 0:
        print("GAME OVER!")
        break

    if len(True_chars) == (len(word)):
     print("YOU WON!")
     break
