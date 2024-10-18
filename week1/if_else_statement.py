def calculate():
    print("Performing calculations...\n\n ")
    print("Activity completed!\n")

def read():
    print("Performing activity...\n\n")
    print("Activity completed!\n")

def main():
    answer = input("Please enter the activity to be performed: ")
    if answer == "calculate":
        calculate()
    elif answer == "read":
        read()
    else:
        print("ERROR...\n\n")
        print("Learn how to type...\n\n")

main()
