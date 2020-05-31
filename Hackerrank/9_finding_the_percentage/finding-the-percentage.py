if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = 0
    for value in student_marks[query_name]:
        average += value
    average = float(average)/3.0
    print("%.2f" % average)