
def display_ladder(steps):
    print(" |   | ")
    print(" |---| ")

def create_ladder():
    repeat = int(input("How many steps remain?: "))
    for i in range(repeat):
        display_ladder(i)

create_ladder()