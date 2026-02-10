num = [8, 2, 8, 1, 3, 9, 5]
end = len(num)
swapping = True
while swapping:
    swapping = False
    for i in range(1, end):
        if num[i - 1] > num[i]:
            num[i - 1], num[i] = num[i], num[i - 1]
            print(num)
            swapping = True
    end -= 1
print(num)
