answer = int(input("What level of brightness is required?: "))

brightness = 2

print("Adjusting brightness...\n")
for i in range(brightness,(answer+2),2):
    print("Brightness level: " + str("*"*brightness))
    brightness += 2
print("\nAdjustments complete!")
