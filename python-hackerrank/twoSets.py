def getTotalX(a,b): #NEEDED AI FOR THE LAST BLOCK OF CODE, CHECKING WHETHER "HOW MANY FACTORS ACTUALLY DIVIDE ME?"
    possibleFactors = []
    for i in range(max(a),min(b)+1): # i represents each integer between the largest value in 'a' and the smallest value in 'b'
        for j in a:
            if (i%j) == 0:
                if i not in possibleFactors:
                    possibleFactors.append(i) # adds all factors for all integers in 'a'
            #     print(f"yes, {j} goes into {i}")
            # else:
            #     print(f"no, {j} does not go into {i}")
    # print(f"first sweep: {possibleFactors}")

    actualFactors = []
    for i in possibleFactors:
        for j in a:
            # print(f"\n{i} divide by {j}")
            if (i%j) != 0:
                # print(f"{j} does not go into {i}")
                if i in actualFactors:
                    # print(f"removing {j} from second sweep")
                    actualFactors.remove(i)
                break
            else:
                # print(f"{j} goes into {i}, adding to second sweep")
                if i not in actualFactors:
                    actualFactors.append(i)
    # print(f"second sweep: {actualFactors}")

    count = 0
    for i in actualFactors:
        dividesAll = True
        for j in b:
            if j % i != 0:
                dividesAll = False
                break
        if dividesAll:
            count += 1
    return count
    

a = [2, 6]
b = [24, 36]
print(getTotalX(a,b))

# --------- MORE EFFICIENT SOLUTION ------------
def getTotalX(a, b):
    count = 0
    for x in range(max(a), min(b) + 1):
        ok = True
        for i in a:
            if x % i != 0:
                ok = False
                break
        if ok:
            for j in b:
                if j % x != 0:
                    ok = False
                    break
        if ok:
            count += 1
    return count