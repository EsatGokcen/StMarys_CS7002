answer = int(input("How far are we from the cave?: "))

word = "steps"

for i in range(answer):
    if answer - i > 1:
        print(str(answer - i) + f" {word} remaining.")
    elif answer - i <= 1:
        word = "step" 
        print(str(answer - i) + f" {word} remaining.")
    else:
        print("ERROR...")




"""
word = ""

for i in range(answer):
    if i < 1:           
        word = "steps" 
    else:
        "step" 
    print(str(i+1) + f" {word} remaining.")
    i += 1
print("We have reached the cave.")
    
"""