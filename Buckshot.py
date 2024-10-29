from itertools import permutations
import re
def invalid_Count(total): #Total bullets cannot exceed 8 
    return total > 8
def is_Valid_Bullet(bullet): #Bullet count must be a digit and between 1 and 5
    return bullet.isdigit() and 1 <= int(bullet) <=5 
def validate_Bullets(): #Prompt user for bullet count
    while True: #Asks & validates for a live bullet count
        l = input("How many live bullets? ") 
        if (is_Valid_Bullet(l)):
            l = int(l)
            break
        print("Invalid input")
    while True: #Asks & validates for a blank bullet count
        b = input("How many blank bullets? ")
        if (is_Valid_Bullet(b)):
            b = int(b)
            break
        print("Invalid input")
    return b, l #Return bullet count 
def is_Valid_Turn(turn, blank, live):
    turn =turn.lower() #.lower() to match string
    if (turn =="b"): #returns if the blank count is below 0
        return blank > 0
    elif (turn =="l"):#returns if live count is below 0
        return live > 0
    return False #if it doesn't match either, it's invalid
def calc_Liv(live, total):
    return round((live/total), 4) * 100; #Returns the percent of it being a live
def show_Poss(blank,live,total):
    bullets = ['L'] * live + ['B'] * blank #Represents B as blanks and L as Lives
    possib = set(permutations(bullets, total)) #Generates all permutations of bullets
    blankf = [''.join(x) for x in possib if x[0] == "B"] #Formats each possibility of it being blank first
    livef = [''.join(x) for x in possib if x[0] == "L"]#Formats each possibility of it being live first
    return {"First Bullet Blank": blankf, "First Bullet Live": livef} #returns formatted possibilities    
#main
while True:
    b, l = validate_Bullets()#sets blank and live amounts
    t = b + l #total = blanks + lives
    if (invalid_Count(t)): #check if total is above 8
        print("Total bullets cannot exceed 8")
        continue 
    for x in range (t): #For each bullet
        print(f"{calc_Liv(l, t)}% chance that next bullet is live") #Show the possibility of it being a live
        outcomes = show_Poss(b,l,t)
        print("Next Bullet Blank:" , outcomes["First Bullet Blank"]) #Shows all possibilities of next bullet being live
        print("Next Bullet Live:" , outcomes["First Bullet Live"]) #Shows all possibilities of next bullet being blank
        
        while True: #Ask & validate user's in game turns
            turn = input("Was it a blank or live? (B or L): ")
            if (is_Valid_Turn(turn,b,l)): #break if it's a valid turn
                break
            print("Invalid input or bullet count below zero") #otherwise invalid input
        
        if (turn.lower() == "b"): #if turn was a blank, subtract 1 from blank
            b -= 1
        elif (turn.lower() == "l"):#if turn was a live, subtract 1 from live
            l -= 1
        t -=1 #subtract 1 from total
        print(f"Blanks left: {b}, Lives left: {l}") #indicate how many blanks and lives are left
    break #breaks intial while loop
