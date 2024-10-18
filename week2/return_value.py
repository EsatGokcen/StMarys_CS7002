
def average_weight(w_Beep , w_Bop): #weight of Beep and Bop
    average = float(w_Beep + w_Bop) / 2
    return average

wbeep = float(input("Enter the weight of Beep (Kg): "))
wbop = float(input("Enter the weight of Bop (Kg): "))

average = average_weight(wbeep,wbop)
print(average) #for some reason