import random
randnumber = random.randint(1,100)
print(randnumber)  #remove this line to hide the random number.
userguesse = None
guesse = 0

while(userguesse!=randnumber):
    guesse += 1
    userguesse = int(input("Enter the number = "))
    if(userguesse==randnumber):
        print("You guessed it right!")
    else:
        if(userguesse<randnumber):
            print("You guessed it wrong,Enter larger number !")
        else:
            print("You guessed it wrong,Enter smaller number !")

print(f"You guessed the number in {guesse} guesses.")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guesse<hiscore):
    print("You have just broke the high score.")
    with open("hiscore.txt","w") as f:
        f.write(str(guesse))