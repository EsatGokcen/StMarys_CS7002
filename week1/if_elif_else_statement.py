answer = input("Please enter a direction (up, down, left, right): ")

switch = True
while switch == True:
    if answer == "up":
        print("I am painting in the upward direction.")
    elif answer == "down":
        print("I am painting in the downward direction.")
    elif answer == "left":
        print("I am painting towards the left.")
    elif answer == "right":
        print("I am painting towards the right.")
    else:
        print("ERROR...\n\n")
        print("Learn to type...\n\n")
        switch = 0