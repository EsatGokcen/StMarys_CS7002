mountains = '''
      __
     /  \\_
    /^    \\
   /    ^  \\_
 _/ ^ ^   ^  \\
/ ^ ^         \\

'''

answer = input("How many mountains should I display? : ")

print("Displaying...")

for i in range(int(answer)):
    print(mountains)

print("Done!")
