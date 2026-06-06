def sockMerchant(n, ar):
    counts = {}
    for sock in ar:
        if sock not in counts:
            counts[sock] = 1
        else:
            counts[sock] += 1
    # print(pairs)
    count = 0
    for socks in counts.values():
        # print(socks//2)
        count += (socks//2)
    return count
                
            
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n,ar))