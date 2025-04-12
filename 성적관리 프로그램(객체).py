class Student: #학생 클래스 선언
    def __init__(self, student_id, name, english, c_lang, python_score):
        self.id = student_id
        self.name = name
        self.english = english
        self.c_lang = c_lang
        self.python = python_score
        self.total = 0
        self.average = 0.0
        self.grade = 'F'
        self.rank = 1

    def calculate_total_and_average(self): # 모든 과목 점수합산 과 평균 점수
        self.total = self.english + self.c_lang + self.python
        self.average = self.total / 3.0

    def calculate_grade(self): # 점수에 따른 등급 선정
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def display(self):
        print(f"{self.id:<10}{self.name:<10}{self.english:<8}{self.c_lang:<8}"
              f"{self.python:<8}{self.total:<8}{self.average:<8.2f}"
              f"{self.grade:<6}{self.rank}")


class StudentManager: # 학생들의 정보를 입력받는 클래스
    def __init__(self):
        self.students = []

    def input_students(self, count=5):# 학생들의 정보 입력
        for i in range(count):
            print(f"\n[{i+1}번째 학생 입력]")
            student_id = input("학번: ")
            name = input("이름: ")
            english = int(input("영어 점수: "))
            c_lang = int(input("C-언어 점수: "))
            python_score = int(input("파이썬 점수: "))
            student = Student(student_id, name, english, c_lang, python_score)
            student.calculate_total_and_average()
            student.calculate_grade()
            self.students.append(student)
        self.calculate_ranks()

    def calculate_ranks(self):
        for s in self.students:
            s.rank = 1
        for i in range(len(self.students)):
            for j in range(len(self.students)):
                if self.students[i].total < self.students[j].total:
                    self.students[i].rank += 1

    def display_all(self):
        print("\n[학생 성적 출력]")
        print(f"{'학번':<10}{'이름':<10}{'영어':<8}{'C언어':<8}{'파이썬':<8}"
              f"{'총점':<8}{'평균':<8}{'학점':<6}{'등수'}")
        print("-" * 70)
        for s in self.students:
            s.display()

    def insert_student(self): # 학생들의 정보를 저장하는 함수
        print("\n[학생 추가]")
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어 점수: "))
        c_lang = int(input("C-언어 점수: "))
        python_score = int(input("파이썬 점수: "))
        student = Student(student_id, name, english, c_lang, python_score)
        student.calculate_total_and_average()
        student.calculate_grade()
        self.students.append(student)
        self.calculate_ranks()

    def delete_student(self, student_id): # 학생의 정보를 삭제하는 함수
        before_count = len(self.students)
        self.students = [s for s in self.students if s.id != student_id]
        after_count = len(self.students)
        if before_count == after_count:
            print("해당 학번의 학생이 없습니다.")
        else:
            print(f"{student_id} 학생 삭제 완료.")
            self.calculate_ranks()

    def search_by_id(self, student_id): #학번으로 학생을 검색하는 함수
        for s in self.students:
            if s.id == student_id:
                print("\n[학번 검색 결과]")
                s.display()
                return
        print("해당 학번의 학생이 없습니다.")

    def search_by_name(self, name): # 이름으로 학생을 검색하는 함수
        found = False
        print("\n[이름 검색 결과]")
        for s in self.students:
            if s.name == name:
                s.display()
                found = True
        if not found:
            print("해당 이름의 학생이 없습니다.")

    def sort_by_total(self): # 학생들을 총점기준으로 정렬하는 함수
        self.students.sort(key=lambda s: s.total, reverse=True)
        print("\n[총점 기준 정렬 완료]")
        self.calculate_ranks()

    def count_above_80(self): # 80점 이상의 학생을 검색하는 함수
        count = sum(1 for s in self.students if s.average >= 80)
        print(f"\n평균 80점 이상 학생 수: {count}명")


def main(): # 메인함수 실행
    manager = StudentManager()
    while True:
        print("\n====== 성적 관리 프로그램 ======")
        print("1. 초기 데이터 입력")
        print("2. 전체 출력")
        print("3. 학생 추가")
        print("4. 학생 삭제")
        print("5. 학번으로 검색")
        print("6. 이름으로 검색")
        print("7. 총점 기준 정렬")
        print("8. 80점 이상 학생 수")
        print("0. 종료")
        choice = input("선택: ")

        if choice == '1':
            manager.input_students()
        elif choice == '2':
            manager.display_all()
        elif choice == '3':
            manager.insert_student()
        elif choice == '4':
            sid = input("삭제할 학번: ")
            manager.delete_student(sid)
        elif choice == '5':
            sid = input("검색할 학번: ")
            manager.search_by_id(sid)
        elif choice == '6':
            name = input("검색할 이름: ")
            manager.search_by_name(name)
        elif choice == '7':
            manager.sort_by_total()
        elif choice == '8':
            manager.count_above_80()
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
