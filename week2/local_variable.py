
max_steps = 10

def cross_bridge(steps=5):
    if steps > 5: 
        steps = 5
    if steps < 0: 
        steps = 0

    for step in range((steps+1)):
        if step == 0:
            pass
        elif step == 1:
            print(f"Taken {step} step.")
        else:
            print(f"Taken {step} steps.")

    steps_remaining = max_steps - (steps+1)
    if steps_remaining <= 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

cross_bridge(steps=3)
cross_bridge(steps=7)