students = []

def input_students():
    for _ in range(5):
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))
        total, average = calculate_total_average(english, c_lang, python)
        grade = calculate_grade(average)
        students.append({"학번": student_id, "이름": name, "영어": english, "C-언어": c_lang, "파이썬": python, "총점": total, "평균": average, "학점": grade, "등수": 1})

def calculate_total_average(english, c_lang, python):
    total = english + c_lang + python
    average = total / 3
    return total, average

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_ranks():
    students.sort(key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(students):
        student['등수'] = i + 1

def display_students():
    print("\n학생 목록:")
    for student in students:
        print(student)

def insert_student():
    student_id = input("학번: ")
    name = input("이름: ")
    english = int(input("영어 점수: "))
    c_lang = int(input("C-언어 점수: "))
    python = int(input("파이썬 점수: "))
    total, average = calculate_total_average(english, c_lang, python)
    grade = calculate_grade(average)
    students.append({"학번": student_id, "이름": name, "영어": english, "C-언어": c_lang, "파이썬": python, "총점": total, "평균": average, "학점": grade, "등수": 1})
    calculate_ranks()

def delete_student(student_id):
    global students
    students = [s for s in students if s['학번'] != student_id]
    calculate_ranks()

def search_student(key, value):
    return [s for s in students if s[key] == value]

def count_high_scores():
    return sum(1 for s in students if s['평균'] >= 80)

def sort_by_total():
    students.sort(key=lambda x: x['총점'], reverse=True)
    calculate_ranks()