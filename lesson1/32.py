file = open('media/freqs.txt', 'r')
thresh = float(input())
ans = ""
for line in file:
    line = line.split(";")
    for elem in line:
        if float(elem) <= thresh:
            ans += (elem+" ")
print(ans)
