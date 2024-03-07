alp = ord("a")
alphabet = ''.join([chr(i) for i in range(alp, alp+27)])
inp = str(input())
point = alphabet.index(inp[0])+1+int(inp[1])
if point%2 == 0:
    print("black")
else:
    print("white")






