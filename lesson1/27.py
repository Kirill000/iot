def volume(*args):
    if len(args) == 2:
        return args[0]*args[1]
    else:
        return args[0]*args[1]*args[2]

inp = list(map(int, input().split()))
if len(inp) == 2:
    print(volume(inp[0], inp[1]))
else:
    print(volume(inp[0], inp[1], inp[2]))