
#Create a program that will play the “Tom and Jerry” game with the user. The game works like this:
#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
#For every digit that the user guessed correctly in the correct place, they get a “Jerry”. 
#For every digit the user guessed wrongly, they get a “Tom”.
#Every time the user makes a guess, tell them how many “Jerry” and “Tom” they have. 
#Once the user guesses the correct number, the game is over. 




import random

def welcome_screen():
    print("Welcome to the 4 Jerries Game!")
    print("For every number in a wrong place, You get a Tom")
    print("For every number in a right place, You get a Jerry")
    print("You win and game ends, when you get 4 Jerries")
    print("Let's Play. Give me your Best Guess!")

def generate_random_number():
    sec_num = random.randint(1000,9999)
    sec_num = str(sec_num)
    list1 = []
    for i in sec_num:
        list1.append(i)
    return list1

def check_num(num, hidden_number):
    
    Jerry = 0
    Tom = 0
    cnt = 0
    
    for i in hidden_number:
         
        if i in set(num) and hidden_number[cnt] == num[cnt]:
            Jerry += 1
            cnt += 1
        else:
            cnt += 1
    
    print (f"{Jerry} Jerry, {4-Jerry} ")
    print("Your Guess isn't queit right. Try again!")

def main():
    welcome_screen()
    guesses = []
    hidden_number = generate_random_number()
    print(hidden_number) #if need to know the hidden number
    print()
    guessed = False
    while not guessed:
        user_guess_list = []
        user_guess = (input("Guess a 4 digit number: "))
        for x in user_guess:
            user_guess_list.append(x)
        guesses.append(user_guess_list)
        if user_guess_list == hidden_number:
            print("That's it!  4 Jerry, and 0 Tom!!")
            print(f"It took you {len(guesses)} tries")
            guessed = True
        elif len(user_guess) == 4 and user_guess.isnumeric():
            result = check_num(user_guess_list, hidden_number)
        else:
            print("4 digit number only please")          
         
main()