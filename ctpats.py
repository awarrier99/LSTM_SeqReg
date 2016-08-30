import string


with open("output.txt", 'r') as ip:
    x = ip.read()

caps = string.ascii_letters.upper()

ind = 0
count = 0
trips = []

while True:
    temp = x[ind:ind + 3]
    good = True
    for let in temp:
        if let not in caps:
            good = False
    if good:
        count++
        trips.append(temp)
    ind++
    if (ind + 3) > len(x):
        break

sys.stdout.write(trips)
