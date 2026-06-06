def pageCount(n,p):
    count = [-1,-1]
    front = [[i,i+1] for i in range(0,n+1,2)]
    print(front)
    for page in front:
        count[0] += 1
        if p in page:
            break
    print(f"took {count[0]} turns to get to page {p}")


    back = []
    if n%2==1:
        for j in range(n,0,-2):
            back.append([j,j-1])
    else:
        back.append([n+1,n])
        for j in range(n-1,0,-2):
            back.append([j,j-1])
    print(back)
    for page in back:
        count[1] += 1
        if p in page:
            break
    print(f"took {count[1]} turns to get to page {p}")

    return min(count)

n = 10 # number of pages
p = 9 # page to get to

print(pageCount(n,p))

def pageCount(n,p):
    count = [-1,-1]
    front = [[i,i+1] for i in range(0,n+1,2)]
    # print(front)
    for page in front:
        count[0] += 1
        if p in page:
            break
    # print(f"took {count[0]} turns to get to page {p}")


    back = []
    if n%2==1:
        for j in range(n,0,-2):
            back.append([j,j-1])
    else:
        back.append([n+1,n])
        for j in range(n-1,0,-2):
            back.append([j,j-1])
    # print(back)
    for page in back:
        count[1] += 1
        if p in page:
            break
    # print(f"took {count[1]} turns to get to page {p}")

    return min(count)