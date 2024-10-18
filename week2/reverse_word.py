answer = input("What phrase do you see?: ")

print("Reversing...\n")

for i in range(len(answer)-1, -1, -1):
    print(answer[i], end="")

print("\n\nDone!")