def adventure():
    print("I like adventure books!")
    print("I finished reading the book!")

def romance():
    print("I like romance books!")
    print("I finished reading the book!")

def main():
    answer = input("Please enter the genre: ")
    if answer == "adventure":
        adventure()
    elif answer == "romance":
        romance()
    else:
        print("ERROR...\n\n")
        print("Learn how to type...\n\n")

main()
        