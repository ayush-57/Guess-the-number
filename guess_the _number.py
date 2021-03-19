print("###### GUESS THE NUMBER #######")
print("You Have 6 Chances to guess ")
secret_number=15
chances=6
while(True):
    print("Enter the number you want to guess : ")
    x=int(input())
    chances=chances-1

    if x>18:
        print("Your guessed number is bigger")
        print("you have", chances, "chances left")
    elif x<=18 and x>=16:
        print("Ohh,You are near to the answer")
        print("you have", chances, "chances left")
        continue
    if x<12:
        print("your guessed number is smaller")
        print("you have", chances, "chances left")
    elif x >=12 and x <= 14:
        print("Ohh,You are near to the answer")
        print("you have", chances, "chances left")
        continue
    if x==secret_number:
        print("Congrats!!!! You guessed the correct number")
        print("you completed the game in",6-chances,"chances")
        break
    if chances==0:
        print("YOU HAVE NO CHANCES LEFT\n***** GAME OVER ******")
        break
