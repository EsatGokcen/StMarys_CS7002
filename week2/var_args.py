
#even ints for Beep / odd ints for Bop

def climb(*args):
    Beep = 0
    Bop = 0

    for num in args:
        if num % 2 == 0: # % is the modulus operator: it get the remainder of the division
            Beep += num
        else:
            Bop += num
    
    if Beep > Bop:
        print("Beep is closer to the top than Bop.")
    elif Bop > Beep:
        print("Bop is closer to the top than Beep.")
    elif Bop == Beep:
        print("Both are the same distance from the top.")
    else:
        print("Error...")


climb(1, 2, 3, 4)
climb(1, 1, 3, 2)
climb(1, 3, 2, 2)
