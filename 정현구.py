class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  # 영어, C-언어, 파이썬 성적
        self.total = sum(scores)
        self.average = self.total / len(scores)
        self.grade = self.calculate_grade()
        self.rank = 0  # 초기 등수 설정

    def calculate_grade(self):
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'

# 학생 정보 입력
students = []
n = 5  # 학생 수
subjects = ["영어", "C-언어", "파이썬"]

for i in range(n):
    name = input(f"{i+1}번째 학생 이름: ")
    scores = [int(input(f"{name}의 {subject} 점수: ")) for subject in subjects]
    students.append(Student(name, scores))

# 등수 계산
total_scores = [student.total for student in students]
sorted_scores = sorted(total_scores, reverse=True)

for student in students:
    student.rank = sorted_scores.index(student.total) + 1

# 결과 출력
print("\n학생 성적 결과")
print("이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
for student in students:
    print(f"{student.name}\t{student.scores[0]}\t{student.scores[1]}\t{student.scores[2]}\t"
          f"{student.total}\t{student.average:.2f}\t{student.grade}\t{student.rank}")