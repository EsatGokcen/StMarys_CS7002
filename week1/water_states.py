answer = int(input("Please enter the water temperature: "))

def current_state():
    if answer < 0:    
        print("Current state is: Solid\n")
    elif answer > 99:
        print("Current state is: Gas\n")
    else:    
        print("Current state is: Liquid\n")

def drinkable():
    if answer < 0 or answer > 99:
        print("The water is not consumable\n")
    else:
        print("The water is consumable\n")

current_state()
drinkable()