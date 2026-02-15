ls = [1, 3, 14, 22, 35, 41, 58, 68, 91]
target = 57
low = 0
high = len(ls) - 1
while low < high:
    median = (low + high) // 2
    print(f"low={low}, high={high}, median={median}, ls[median]={ls[median]}")
    if target == ls[median]:
        print(median)
        break
    elif target > ls[median]:
        low = median + 1
    elif target < ls[median]:
        high = median - 1
else:
    print("Not found")
