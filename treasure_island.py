print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_turn = input(" Do you want to take left or right? L or R \n ").lower()
if first_turn == "l":
    swim_wait = input("You have reached a large river. Do you want to try and swim or would you prefer to wait? W or S\n ").lower()
    if swim_wait == "w":
        choose_door = input("There are three doors in front of you - Red, Yellow and Blue. Which door do you go through? R, Y or B \n").lower()
        if choose_door == "y":
            print("You have reached the treasure room! YOU WIN! (game is still over though)")
            
        elif choose_door == "r":
            print("You fall into a firey abyss and it is GAME OVER.")
            
        elif choose_door == "b":
            print("You were eaten by wild beasts, GAME OVER")

        else:
            print("GAME OVER (try following instructions better...")
    else:
        print("You were attacked by an overly aggresive trout. GAME OVER.")
    
else:
    print("You went right... You fell into a hole. GAME OVER. (Should've gone left, really...)")