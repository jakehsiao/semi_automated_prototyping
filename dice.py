import random

count = 1
while True:
    line = input()
    if line.isdigit():
        count = int(line)

    print(" ".join([str(random.randint(1,6)) for i in range(count)]))
