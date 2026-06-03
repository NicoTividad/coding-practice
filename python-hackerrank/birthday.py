def birthday(s, d, m):
    count = 0
    print(f"length of array is {len(s)}")
    for i in range(len(s)-m+1):
        print(f"\niteration {i}")
        sum = 0
        for num in range(m):
            print(f"adding {s[i+num]}")
            sum += s[i+num] 
        print(f"sum: {sum}")
        if sum == d:
            count += 1
    
    print(f"there are {count} ways to add up to {d}")
    
    return count

s = [1,2,1,3,2]
d = 3 # total the squares has to add up to
m = 2 # number of consecutive squares
print(birthday(s,d,m))

def birthday(s, d, m):
    count = 0
    for i in range(len(s)-m+1):
        sum = 0
        for num in range(m):
            sum += s[i+num] 
        if sum == d:
            count += 1
    
    return count