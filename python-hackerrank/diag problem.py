arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
diags = [0,0]
for i in range(len(arr)):
    for j in range((len(arr[0]))):
        # print(f"{i}, {j}")
        if i == j:
            diags[0] += arr[i][j]
        if (len(arr)-1-i) == (0+j):
            # print([i,j])
            diags[1] += arr[i][j]

print(len(arr))
print(diags)
print(abs(diags[0] - diags[1]))
