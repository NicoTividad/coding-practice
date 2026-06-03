def birthdayCandles(candles):
    n = max(candles)
    count = 0
    for i in candles:
        if i == n:
            count += 1
    print(count)
    

candles = [3,1,2,3]
birthdayCandles(candles)