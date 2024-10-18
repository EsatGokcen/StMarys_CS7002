import random

var = True

while var == True:
    print("What would you like to see? ")
    print("[1] Random Number\n[2] Random Word")

    answer = input("Please enter your selection: ")
    if answer.isnumeric():
        if answer == "1":
            print(random.randint(1,100))
            var = False
        elif answer == "2":
            print(random.choice(["blue","hello","programming","fun"]))
            var = False
    else:
        print("ERROR...")


    
        



