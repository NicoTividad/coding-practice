def countApplesAndOranges(s, t, a, b, apples, oranges):
    count = [0,0]
    for i in range(len(apples)):
        apples[i] += a
        if apples[i] >= s and apples[i] <= t:
            count[0] += 1
    for j in range(len(oranges)):
        oranges[j] += b
        if oranges[j] >= s and oranges[j] <= t:
            count[1] += 1
    print(count[0])
    print(count[1])
    

s, t, a, b = 7, 10, 4, 12
apples, oranges = [2, 3, -4], [3, -2, -4]

countApplesAndOranges(s, t, a, b, apples, oranges)