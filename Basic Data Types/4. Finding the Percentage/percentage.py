if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Calculate the average of the marks array for the given student name
    marks = student_marks[query_name]
    average_mark = sum(marks) / len(marks)

    # Print the average with 2 decimal places
    print("{:.2f}".format(average_mark))
