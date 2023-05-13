students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    
second_lowest_score = sorted(set([score for name, score in students]))[1]
second_lowest_students = sorted([name for name, score in students if score == second_lowest_score])

for student in second_lowest_students:
    print(student)
