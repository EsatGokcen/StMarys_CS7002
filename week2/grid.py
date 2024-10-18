
rows = input("How many rows should I display?: ")
columns = input("How many columns should I display?: ")

print("Here I go...\n\n")

for count in range(int(rows)):
    for number in range(int(columns)):
        print(f" \U0001F974 |", end="")
    print()

print("\n\nDone.")



           
