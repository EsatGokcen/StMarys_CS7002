# LECTURE ONE TO DO
# Display messages.
# '''
print()
print("system failure imminent!")
print("system reboot required.")
print()
print("\U0001F916")
print()
print("    ***    ")
print(" *       * ")
print("*  O   O  *")
print("*    ^    *")
print(" *  ---  * ")
print("    ***    ")
print()
print("#" * 39)
print("# system reboot has been initiated... #")
print("#                                     #")
print("#    - rebooting sensory system       #")
print("#    - rebooting output motors        #")
print("#    - rebooting hover engine         #")
print("#                                     #")
print("# system reboot completed.            #")
print("#" * 39)
print("new\nline")
# Display status.
print("#" * 22)
print("Battery Level: 100% \U0001F50B")
print("Volume Level:  50%  \U0001F50A")
print("Light Level:   30%  \U0001F4A1")
print("#" * 22)
# Display status.
print("#" * 33)
print("#", "\U0001F50B 100%", "\U0001F50A 50%", "\U0001F4A1 30%", "#", sep=" | ")
print("#" * 33)
# VARIABLES AND STORING DATA
# Display settings.
battery_level = 100
volume_level = 10
light_level = 10

print("#" * 26)
print("# Diagnostics:           #")
print("#", "-" * 22, "#")
print("# Battery Level (%):", battery_level, "#")
print("# Volume Level (%): ", volume_level, " #")
print("# Light Level (%):  ", light_level, " #")
print("#" * 26)



# '''
# MY OWN PROJECT FOR LECTURE1

'''

print("Hello, welcome to St Marys Computer Science postgrad!")

first_name = input("What is your name? ")
print("Hello " + first_name + ". I can't wait to learn Python with you!")

Question1 = input("Can I ask you some questions to get to know you better? yes/no ")

if Question1 == "yes":
    last_name = input("What is your last name? ")
    age = input("How old are you " + first_name + "? ")

    if int(age) > 17:
        print("You qualify for the next step.")

        email = input("What is your email? ")
        credit_card = input("What is your credit card number? ")

        print("It is nice to meet you " + first_name + " " + last_name + ". You are " + str(age) + " years old.")
        print("Your email is " + email)
        print("Credit card num: " + credit_card)
        print("Credit card balance: 0")
    elif int(age) <= 17:
        years_left = 18 - int(age)
        print("Apologies, you still have " + str(years_left) + " years left to qualify for this scam.")
        print("You can still get your parents to complete the form!")
else:
    print("No worries, have a nice day...")

'''





