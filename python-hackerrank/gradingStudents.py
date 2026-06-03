def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        round = 5 - (grades[i] % 5)
        if round < 3:
            grades[i] += round
    return grades

grades = [73, 67, 38, 33]
result = gradingStudents(grades)
print(result)