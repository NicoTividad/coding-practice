def kangaroo(x1, v1, x2, v2): #NEEDED AI FOR HELP WITH THIS ONE
    n = 0
    while True:
        if x1 == x2:
            binary = 1
            break

        old_diff = abs(x1 - x2)
        x1 += v1
        x2 += v2
        diff = abs(x1-x2)
        n += 1      

        if old_diff <= diff:
            binary = 0
            break

    if binary == 0:
        return "NO"
    else:
        return "YES"
    # if (x1 >= x2 and v1 >= v2) or (x1 <= x2 and v1 <= v2):
    #     print("NO")
    # else:
    #     print("YES")

x1, v1 = 0, 3
x2, v2 = 4, 2
print(kangaroo(x1, v1, x2, v2))
# print(abs(-1-3))