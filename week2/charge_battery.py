answer = int(input("How many lines should be charged? : "))

count = 0

while count <= answer:
    print("Charging: " + "🔋" * count)
    count += 1

print("The battery is fully charged.")
