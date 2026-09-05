'''
5 chanes
1: 100 points
2: 80 points
3: 60
4: 40
5: 20
You lost
hidden_number=65
guess a number between 1 to 100
75
Your guess is high
35
you guess is low
55
your guess is low
60
your guess is low
70
your guess is high

'''
import random
hidden_number=random.randint(1,100)
# print(hidden_number)

score=100
for i in range(5):
    guess=int(input("Guess a numbe between 1 to 100: "))
    if guess==hidden_number:
        print("You Won!")
        print("Score: ",score)
        break
    elif guess>hidden_number:
        print("Hint: Your guess is High")
        score-=20
    else:
        print("Hint: Your guess is Low")
        score-=20
else:
    print("All Chances are gon!")
    print("You Lost!")
    print("Hidden Number:",hidden_number)



