# ROCK, PAPER SCISSORS
# passes down from the acient chinese dynasty
#shoushilling is now better known as rock , paper and scissors
#this code implements the version of the game that is you against the
# computer.

import random
winner = ''


# above is the first stage of our game.
#we first start with setup by first
#importing the random module and setting up the winner variable

random_choice = random.randint(0, 2)

if random_choice == 0:
   computer_choice = 'rack'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'
    
#the computer randomly chooses rock, paper and scissors by generationg
#a random number  from 0 to 2 and mapping  that to the corresponding string

user_choice = '' # this is called empty string
while(user_choice != 'rock' and
      user_choice != 'paper' and
      user_choice != 'scissors' ): 
    user_choice = input('rock, paper or scissors? ')

#users choice is straightforward

if computer_choice == user_choice:
    winner = 'Tie' # if computer choice is equal to user choice there is a tie
elif computer_choice == 'rock' and user_choice == 'paper' :
    winner = 'computer'
elif computer_choice == 'paper' and user_choice == 'scissors' :
    winner = 'computer'
elif computer_choice == 'scissors' and user_choice == 'rock' :
    winner = 'computer'

#this is setting out the computers as a winner if the coomputer chooses
# either roc,  paper and scissors
   
else :
    winner ='Osang' # if the computer doesn't win the the user wins



    
if winner == 'Tie' : # here we announce the winner as a tie
    print('we both choose', computer_choice + ',play again')
else:
    print(winner, 'won. The computer choose something like', computer_choice +  '.')
