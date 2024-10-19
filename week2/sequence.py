
marker = input("Please enter marker: ").lower()
sequence = input("Please enter sequence: ").lower()

distance = 0
is_counting = False

for character in sequence:
    if character == marker:
        is_counting = not is_counting
    elif is_counting:
        distance += 1

print(f"The distance between the markers is: {distance}")