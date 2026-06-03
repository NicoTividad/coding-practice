def timeConversion(s):
    modifier= s[-2]
    # print(modifier)
    time = s.strip("APM")
    if modifier.upper() == "A":
        if time[:2] == "12":
            time = time.split(":")
            time[0] = "00"
            return ":".join(time)
        return time
    else:
        if time[:2] == "12":
            return time
        else:
            time = time.split(":")
            time[0] = int(time[0]) + 12
            time[0] = str(time[0])
            return ":".join(time)

s = "12:05:45AM"
result = timeConversion(s)
print(f"{result}\n")


 # MORE EFFICIENT APPROACH
def timeConversion(s):
    period = s[-2:]
    h, m, sec = s[:-2].split(":")
    if period == "AM":
        h = "00" if h == "12" else h
    else:
        h = h if h == "12" else str(int(h) + 12)
    return f"{h}:{m}:{sec}"