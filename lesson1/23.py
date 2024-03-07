def my_filter(a: list=[]):
    string = ""
    for elem in a:
        string += (str(elem*10)+" ")
    return string

print(my_filter([-3, 7, 2, -10, -9, -2, 5, 8, 4, 5]))