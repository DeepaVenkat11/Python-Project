import random
import time
count=1
Name = input("Enter your name please : ")
print(f"Hi! {Name} Welcome to the guessing number game.Please guess a number between 1 to 50")
time.sleep(4)
print("Picking a number..")
time.sleep(2)
guess = int(input("What is your guess? "))
correct_num = random.randint(1,50)
while(guess!=correct_num):
    time.sleep(1)
    if guess < correct_num :
        guess = int(input("Sorry!Your answer is wrong.You need to guess higher "))
        count+=1
    else :
        guess = int(input("Sorry!Your answer is wrong.You need to guess lower "))
        count+=1
if(count<=3):
  coin="Gold "
if(count>3 and count <=6):
    coin="Silver "
if(count>6 and count <=10):
    coin='1 Ruppee '
    
print(f"Great! The number is {guess}.You will get a {coin}coin")
