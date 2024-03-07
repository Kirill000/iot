melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni':
1455,'Si': 1415, 'Be': 1287}
els = list(map(str, input().split()))
first_element = els[0]
second_element = els[1]
print("Temperature of first element is higher on ", melt.get(first_element)-melt.get(second_element), " than second")