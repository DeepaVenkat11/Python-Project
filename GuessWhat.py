import random
Guess = int(input("What is your guess? "))
count = 0
correct_num = random.randint(1,100)
while Guess != correct_num:
    if(Guess<correct_num):
        Guess = (int(input("Your answer is wrong!Guess the highest number : ")))
        count+=1
    else :
        Guess = (int(input("Your answer is wrong!Guess the lowest number : ")))
        count+=1
print(f"Great!! correct answer is {Guess} and it took you {count} guess!")
