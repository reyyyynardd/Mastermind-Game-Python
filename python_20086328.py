#import random library
import random

#define the list of fruits that are used in the programme
fruit_list = ["apple", "banana", "orange", "grape", "peach", "watermelon"]

print ("Welcome to Mastermind!")
print ("By: Reynard Amadeus Rumanouw")
print ("Here is the list of fruits for this game:")
print (fruit_list)

#selection using if-elif statement to read instructions or immediately start
select = input("Would you like to read the rules & instructions of this game or not? (yes/no): ").lower()
if select == "yes":
    print ("1. You are required to guess the order of 4 fruits (code) chosen from the list shown at the start of the program.")
    print ("2. The code will be generated randomly by the computer.")
    print ("3. The code can have repeating fruits.")
    print ("4. Your guess must include an order of 4 fruits.")
    print ("5. You must guess using the fruits from the list given.")
    print ("6. After each guess, the game will tell you how many fruits did you guess in the right place and which fruits you guessed are in the code but in the wrong place.")
    print ("7. There is no limited number of attempts.")
elif select == "no":
    print ("Then let's start the game!")

#user-defined function for creating the code
def code():
    #globalise the list so that it can be used in other user-defined functions
    global fruit_code
    #uses random library to choose a list of 4 fruits
    fruit_code = random.choices(fruit_list, k=4)

#user-defined function for player's guess
def guess():
    print ("You are required to enter your guess below: ")
    global guess_list
    #asks user for input to guess the code
    guess_list = input().lower().split()
    print ("Your guess is: ", guess_list)

#user-defined function for comparing player's guess and code
def compare_list():
    #list created used to compare & calculate correct fruits wrong place
    compare_fruit_list = ["","","",""]
    #variable initialized for correct fruits correct place
    correct_fruit_num = 0
    
    #for loop & if statement used to calculate correct fruits correct place
    for i in range(4):
        if guess_list[i] == fruit_code[i]:
            correct_fruit_num += 1
            #replaces contents of compare_fruit_list with guess_list so that it can be compared to check for correct fruits wrong place
            compare_fruit_list [i] = guess_list [i]
    #prints how many fruit(s) are correctly placed
    print ("Correct fruit(s) in the correct place: ", correct_fruit_num)
    
    #two empty lists created for comparison without changing the original lists
    code_check_list = []
    guess_check_list = []
    #variable initialized for correct fruit wrong place
    wrong_fruit_num = 0
    
    #for loop to append check lists with contents of original lists
    for i in range(4):
        code_check_list.append(fruit_code[i])
        guess_check_list.append(guess_list[i])
    
    #for loop to replace contents of check lists if they are similar to the comparison list
    for i in range(4):
        if code_check_list[i] == compare_fruit_list[i]:
            code_check_list[i] = ""
        if guess_check_list[i] == compare_fruit_list[i]:
            guess_check_list[i] = ""
    
    #for loop to compare the leftover fruits to calculate how many are correct but in the wrong place
    for i in range(4):
        if guess_check_list[i] != code_check_list[i]:
            if guess_check_list[i] in code_check_list:
                wrong_fruit_num += 1
    #prints how many fruit(s) correct but wrongly placed   
    print("Correct fruit(s) but in the wrong place: ", wrong_fruit_num)

#while loop when the programme is running
while True:
    
    #variable for attempts initialized
    attempts = 0
    #calls user-defined function for code
    code()
    #calls user-defined function for player's guess
    guess()
    attempts +=1
    
    #if statement to compare the number of elements between player's guess and code
    if len(guess_list) != len(fruit_code):
        print ("Invalid guess! You must guess an order of 4 fruits. Try again.")
        attempts -= 1
        continue
    
    #for loop to check validity of fruits that player input   
    for i in range(4):
        if guess_list[i] not in fruit_list:
            print ("Invalid guess! That fruit is not in the list of this game. Try again.")
            attempts -= 1
            break
    
    #calls user-defined function for comparing lists       
    compare_list()
    
    #while loop to count number of attempts if player fails to guess code
    while guess_list != fruit_code:
        
        guess()
        attempts +=1
        
        if len(guess_list) != len(fruit_code):
            print ("Invalid guess! You must guess an order of 4 fruits. Try again.")
            attempts -= 1
            continue
            
        for i in range(4):
            if guess_list[i] not in fruit_list:
                print ("Invalid guess! That fruit is not in the list of this game. Try again.")
                attempts -= 1
                break
            
        compare_list()
            
    #if statement to display number of attempts taken for when player correctly guesses code            
    if attempts == 1:
        print("Congrats! You managed to decipher the code in just 1 attempt!")
    else:
        print("Congrats! You managed to decipher the code in ", str(attempts), "attempts!")
    
    #if statement for player to choose to play again or not   
    if input("Play again? (yes/no) ").lower() != "yes":
            
            break