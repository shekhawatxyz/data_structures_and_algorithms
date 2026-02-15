# ls = [34,12,28,91,55,76,82]
ls = [1, 2, 3, 4, 5]
swapping = True
ll = len(ls) - 1
while swapping:
    swapping = False
    print(f"Starting pass, ll={ll}")
    for i in range(ll):
        if ls[i] > ls[i + 1]:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
            swapping = True
    ll -= 1
print(ls)
