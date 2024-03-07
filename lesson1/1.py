from math import ceil

floors = 8
columns = 4

room = int(input())
if room%8 == 0:
    print(8, ceil(room/8))
else:
    print(room%8, ceil(room/8))