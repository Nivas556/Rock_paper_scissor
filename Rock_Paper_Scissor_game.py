import random
choices=['rock','paper','scissors']
computer=random.choice(choices)
player= False
cpu=0
player_score=0
while True:
    player=input("choose any of one below...\nTo end the game press End\nRock,paper,or scissors:\t")
    #conditions of Rock,paper and scissors
    if player==computer:
        print("It's a Tie..")
    elif player== "Rock":
        if computer=='paper':
            print('You lose!',computer,'covers',player)
            cpu+=1
        else:
            print("you win!",player,'smashes',computer)
            player_score+=1
    elif player=="paper":
        if computer=='scissors':
            print("You Lose!...",computer,"cut",player)
            cpu+=1
        else:
            print('You win!',player,"covers",computer)
            player_score+=1
    elif player=="scissors":
        if computer=="Rock":
            print("You Lose!...",computer,"smashes",player)
            cpu+=1
        else:
            print('You win!',player,"cut",computer)
            player_score+=1
    elif player=='End':
        print('..........The Final scores are as follows..........')
        print(f"CPU:{cpu}")
        print(f"PLAYER:{player_score}")
        break


