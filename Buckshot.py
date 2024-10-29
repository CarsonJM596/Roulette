from itertools import permutations
import re
def invalid_Count(total):
    if (total > 8): #If total bullets above 8, invalid total of bullets
        return True
    return False
def is_Valid_Bullet(bullet):
    reg = r"^[1-5]$" # All allowed versions of input
    return bool(re.match(reg, bullet)) #Return if it matches regex or not
def is_Valid_Turn(turn, blank, live):
    turn = turn.lower() #Lower inputted string to check regex
    reg = r"^(b|l)$" 
    if (turn == "b"):
        blank -=1 #Subtract one from blank
        if (blank < 0): #If blank is under zero, invalid turn
            print("Bullet number cannot go under 0")
            return False
    elif (turn == "l"):
        live -=1 #Subtract one from live
        if (live < 0): #If live is under zero, invalid turn
            print("Bullet number cannot go under 0")
            return False
    return bool(re.match(reg, turn)) #Returns if input matches regex
def calc_Liv(live, total):
    return round((live/total), 4) * 100; #Returns the percent of it being a live
def show_Poss(blank,live,total):
    bullets = ['L'] * live + ['B'] * blank #Represents B as blanks and L as Lives
    possib = set(permutations(bullets, total)) #Generates all permutations of bullets
    blankf = [''.join(x) for x in possib if x[0] == "B"] #Formats each possibility of it being blank first
    livef = [''.join(x) for x in possib if x[0] == "L"]#Formats each possibility of it being live first
    return {"First Bullet Blank": blankf, "First Bullet Live": livef} #returns formatted possibilities    
#main
t = 9 #intiates while loop
while (invalid_Count(t)): #Shotgun can have more than 8 bullets
    l = input("How many live bullets? ") 
    while (is_Valid_Bullet(l)==False): #Catch invalid input
        print("Invalid input") 
        l = input("How many live bullets? ")
    b = input("How many blank bullets? ")
    while (is_Valid_Bullet(b)==False):#Catch invalid input
        print("Invalid input")
        b = input("How many live bullets? ")
    b = int(b) #Turn input into an int
    l= int(l) #Turn input into an int
    t = b + l #Add up to get total amount of bullets
for x in range (0, t): #For each bullet in shotgun
    print(calc_Liv(l,t),"% chance that next bullet is live") #Show the possibility of it being a live
    outcomes = show_Poss(b,l,t)
    print("First Bullet Blank:" , outcomes["First Bullet Blank"])
    print("First Bullet Live:" , outcomes["First Bullet Live"])
    turn = input("Was it a blank or live? (B or L): ") #Ask user what type of bullet it was
    while(is_Valid_Turn(turn,b,l) == False): #Catch invalid input
        print("Invalid input.")
        turn = input("Was it a blank or live? (B or L): ")
    if (turn.lower() == "b"): #if turn was a blank, subtract 1 from blank
        b -= 1
    elif (turn.lower() == "l"):#if turn was a live, subtract 1 from live
        l -= 1
    t -=1 #subtract 1 from total
    print("Blanks left:", b, "Lives left:", l) #indicate how many blanks and lives are left