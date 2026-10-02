import math
import numpy as np

class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def get_gpa(self): return self.__gpa
    def set_gpa(self, gpa): self.__gpa = gpa

    def input(self):
        self.__id = input("Student ID: ").strip()
        self.__name = input("Student Name: ").strip()
        self.__dob = input("DoB (dd/mm/yyyy): ").strip()

    def list(self):
        print(f"ID: {self.__id:<10} | Name: {self.__name:<20} | DoB: {self.__dob:<12} | GPA: {self.__gpa:.1f}")


class Course:
    def __init__(self, course_id="", name="", credits=0):
        self.__idc = course_id
        self.__namec = name
        self.__credits = credits

    def get_idc(self): return self.__idc
    def get_namec(self): return self.__namec
    def get_credits(self): return self.__credits

    def input(self):
        self.__idc = input("Course ID: ").strip()
        self.__namec = input("Course Name: ").strip()
        self.__credits = int(input("Credits: "))

    def list(self):
        print(f"ID: {self.__idc:<10} | Course: {self.__namec:<20} | Credits: {self.__credits}")


class MarkManager:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {} # {course_id: {student_id: mark}}

    # Requirement 1: Round-down mark using math.floor()
    def __round_down(self, mark):
        return math.floor(mark * 10) / 10.0

    # Requirement 2: Calculate GPA using numpy array
    def calculate_gpa(self, student_id):
        marks_list = []
        credits_list = []

        for course in self.__courses:
            c_id = course.get_idc()
            if c_id in self.__marks and student_id in self.__marks[c_id]:
                marks_list.append(self.__marks[c_id][student_id])
                credits_list.append(course.get_credits())

        if not credits_list:
            return 0.0

        # NumPy arrays for weighted average sum(marks * credits) / sum(credits)
        np_marks = np.array(marks_list)
        np_credits = np.array(credits_list)
        
        gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
        return self.__round_down(gpa)

    # Requirement 3: Sort students by GPA descending using numpy
    def sort_students_by_gpa(self):
        # Update GPA for all students first
        for s in self.__students:
            s.set_gpa(self.calculate_gpa(s.get_id()))

        if not self.__students:
            return

        gpas = np.array([s.get_gpa() for s in self.__students])
        sort_indices = np.argsort(gpas)[::-1] # Sort descending index
        self.__students = [self.__students[i] for i in sort_indices]

    def input_students(self):
        num = int(input("Number of students: "))
        for i in range(num):
            print(f"\n--- Student {i+1} ---")
            s = Student()
            s.input()
            self.__students.append(s)

    def input_courses(self):
        num = int(input("Number of courses: "))
        for i in range(num):
            print(f"\n--- Course {i+1} ---")
            c = Course()
            c.input()
            self.__courses.append(c)

    def input_marks(self):
        if not self.__courses or not self.__students:
            print("Please input students and courses first!")
            return

        c_id = input("Enter course ID to input marks: ").strip()
        course_exists = any(c.get_idc() == c_id for c in self.__courses)
        
        if not course_exists:
            print("Course not found!")
            return

        if c_id not in self.__marks:
            self.__marks[c_id] = {}

        print(f"\n--- Entering marks for course {c_id} ---")
        for s in self.__students:
            raw_mark = float(input(f"Mark for {s.get_name()} ({s.get_id()}): "))
            # Apply math.floor round-down
            self.__marks[c_id][s.get_id()] = self.__round_down(raw_mark)

    def list_courses(self):
        print("\n=== COURSE LIST ===")
        for c in self.__courses:
            c.list()

    def list_students(self):
        print("\n=== STUDENT LIST (SORTED BY GPA DESCENDING) ===")
        self.sort_students_by_gpa()
        for s in self.__students:
            s.list()

    def show_marks(self):
        c_id = input("Enter course ID: ").strip()
        if c_id in self.__marks:
            print(f"\n=== MARKS FOR COURSE: {c_id} ===")
            for s in self.__students:
                mark = self.__marks[c_id].get(s.get_id(), "N/A")
                print(f"Student: {s.get_name():<20} (ID: {s.get_id():<8}) -> Mark: {mark}")
        else:
            print("No marks recorded for this course.")


def main():
    manager = MarkManager()
    while True:
        print("\n" + "="*30)
        print(" STUDENT MANAGEMENT SYSTEM ")
        print("="*30)
        print("1. Input Students")
        print("2. Input Courses (with Credits)")
        print("3. Input Marks")
        print("4. List Courses")
        print("5. List Students (Sorted by GPA)")
        print("6. Show Marks")
        print("0. Exit")
        
        choice = input("Choose option: ").strip()
        if choice == '1': manager.input_students()
        elif choice == '2': manager.input_courses()
        elif choice == '3': manager.input_marks()
        elif choice == '4': manager.list_courses()
        elif choice == '5': manager.list_students()
        elif choice == '6': manager.show_marks()
        elif choice == '0':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()