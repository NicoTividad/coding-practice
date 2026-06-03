def minmax(n):
    values = [0,0]
    min = []
    max = []

    for i in sorted(n):
        min.append(i)
    min.pop()
    values[0] += sum(min)

    for j in sorted(n, reverse=True):
        max.append(j)
    max.pop()
    values[1] += sum(max)

    print(f"{values[0]} {values[1]}")


n = [1,2,3,4,5]
minmax(n)
