answer = input("What type of adventure should I have?: ")

if answer == "scary" or answer == "short":
    print("Entering the dark forest!")
elif answer == "safe" or answer == "long":
    print("Taking the safe route!")
else:
    print("\n\nERROR...\n\n")