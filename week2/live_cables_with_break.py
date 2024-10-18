import random
import time

answer = int(input("How many live electric cables must I avoid? : "))

count = 0

while True:
    is_live_cable = random.choice([0, 1])
    if is_live_cable == True:
        count += 1
        print("Avoided live electric cable.")
        time.sleep(1)
    elif is_live_cable == False:
        print("Found dead electric cable.")
        time.sleep(1)
    else:
        print("Something went wrong...")
    if count >= answer:
        print("Finished avoiding live electric cables.")
        break
    
    
