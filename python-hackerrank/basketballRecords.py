def breakingRecords(scores):
    count = [0,0]
    minmaxScores = [scores[0], scores[0]]
    print(f"min/max scores are {minmaxScores}")
    print(scores)
    scores.remove(scores[0])
    for score in scores:
        print(f"\nlooking at {score}")
        print(f"minmax scores are {minmaxScores}")
        if score in minmaxScores:
            continue
        elif score < minmaxScores[0]:
            minmaxScores[0] = score
            count[0] += 1
        elif score > minmaxScores[1]:
            minmaxScores[1] = score
            count[1] += 1
        print(f"count: {count}")

        print(f"we are on {score}")
    return count

scores = [3, 3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(breakingRecords(scores))


def breakingRecords(scores):
    count = [0,0]
    minmaxScores = [scores[0], scores[0]]
    # print(f"min/max scores are {minmaxScores}")
    print(scores)
    scores.remove(scores[0])
    for score in scores:
        # print(f"\nlooking at {score}")
        # print(f"minmax scores are {minmaxScores}")
        if score in minmaxScores:
            continue
        elif score < minmaxScores[0]:
            minmaxScores[0] = score
            count[0] += 1
        elif score > minmaxScores[1]:
            minmaxScores[1] = score
            count[1] += 1
        # print(f"count: {count}")

        # print(f"we are on {score}")
    return scores