import time

answer = input("What strange markings do you see in the cave?: ")

print("Identifying...\n")
time.sleep(1)

index_num = 0

for i in answer:
    print("Index " + str(index_num) + " : " + str(i))
    index_num += 1

if index_num >= len(answer):
    print("\nDone!")