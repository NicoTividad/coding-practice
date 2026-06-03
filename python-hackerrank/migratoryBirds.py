def migratoryBirds(arr):
    birdTypes = {}
    for bird in arr:
        if bird not in birdTypes:
            birdTypes[bird] = 1
        else:
            birdTypes[bird] += 1
    
    maxVal = []
    for type in birdTypes.keys():
        if birdTypes[type] == max(birdTypes.values()):
            maxVal.append(type)

    return min(maxVal)

arr = [1,4,4,4,5,3]
print(migratoryBirds(arr))