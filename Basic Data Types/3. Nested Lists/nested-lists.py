if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    # Find the second lowest grade
    scores = sorted(set([student[1] for student in students]))
    second_lowest_score = scores[1]

    # Extract names of students with the second lowest grade
    second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_score])

    # Print each name on a new line
    for student in second_lowest_students:
        print(student)
