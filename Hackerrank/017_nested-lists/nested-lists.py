if __name__ == '__main__':
    # initialize arrays
    students = []
    scores = []
    result = []
    # populate arrays with inputs
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
    # find second lowest score
    second_lowest = sorted(list(set(scores)))[1]
    # find students with second lowest score
    for student in students:
        if student[1] == second_lowest:
            result.append(student[0])
    # print them in alphabetical order
    for value in sorted(result):
        print(value)