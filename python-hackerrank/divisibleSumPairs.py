def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1):
        print(f"\niteration {i}")
        for j in range(i+1,n):
            print(f"\nadding {ar[i]} with {ar[j]}", end=". ")
            value = ar[i] + ar[j]
            print(f"result is {value}", end=". ")
            if (value%k) == 0:
                print(f"{value} can be divided by {k}")
                count += 1
    return count

n = 6 # length of the array
k = 5 # the dividing integer
ar = [1,2,3,4,5,6] # array with the integers that can be added
print(divisibleSumPairs(n, k, ar))

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            value = ar[i] + ar[j]
            if (value%k) == 0:
                count += 1
    return count


