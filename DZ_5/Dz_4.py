L = [77, 88, 99, 0, 0, 77, 1, 2]
L.sort()
L_iter = iter(L)
L_falses = []
for i in L_iter:
    if i == next(L_iter):
        L_falses.append(i)
for i in L_falses:
    if i in L:
        L.remove(i)
print(L)