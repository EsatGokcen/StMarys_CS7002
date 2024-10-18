#types of triangles: "scalene", "equilateral", or "isosceles"

answer = input("What type of triangle do we have?: ")

if answer == "scalene":
    print("All the sides are different.")
    answer2 = input("Do you wish to see a famous scalene triangle?: ")
    if answer2 == "yes":
        print("Famous scalene triangle: 3, 4, 5")
    else:
        print("No worries...")
elif answer == "equilateral":
    print("All sides are equal")
elif answer == "isosceles":
    print("Two sides are the same")
else:
    ("\n\nNOT VALID ANSWER\n\n")