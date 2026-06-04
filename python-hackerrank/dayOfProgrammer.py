def dayOfProgrammer(year):
    if year == 1918:
        return f'26.09.{year}'

    if year < 1918:
        leap = year % 4 == 0
    else:                               
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    if leap:
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'

year = 1800
print(dayOfProgrammer(year))