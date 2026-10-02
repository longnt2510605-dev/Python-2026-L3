class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    # Polymorphism: Phương thức input() của Student
    def input(self):
        self.__id = input("student id: ").strip()
        self.__name = input("name of student: ").strip()
        self.__dob = input("date of birth (dd/mm/yyyy): ").strip()

    # Polymorphism: Phương thức list() của Student
    def list(self):
        print(f"student id: {self.__id} | name: {self.__name} | dob: {self.__dob}")


class Course:
    def __init__(self, course_id="", name=""):
        self.__idc = course_id
        self.__namec = name

    def get_idc(self):
        return self.__idc

    def get_namec(self):
        return self.__namec

    # Polymorphism: Phương thức input() của Course
    def input(self):
        self.__idc = input("id course: ").strip()
        self.__namec = input("name course: ").strip()

    # Polymorphism: Phương thức list() của Course
    def list(self):
        print(f"course id: {self.__idc} | name: {self.__namec}")


class Mark:
    def __init__(self, student_id="", course_id="", mark_value=0.0):
        self.__id = student_id
        self.__idc = course_id
        self.__mark = mark_value

    def get_id(self):
        return self.__id

    def get_idc(self):
        return self.__idc

    def get_mark(self):
        return self.__mark

    def input(self):
        self.__id = input("student id: ").strip()
        self.__idc = input("id course: ").strip()
        self.__mark = float(input("enter mark: "))


class SchoolManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = []

    def input_student(self):
        numberS = int(input("number of students: "))
        for _ in range(numberS):
            s = Student()
            s.input()
            self.__students.append(s)

    def input_courses(self):
        numberC = int(input("number of courses: "))
        for _ in range(numberC):
            c = Course()
            c.input()
            self.__courses.append(c)

    def input_mark(self):
        m = Mark()
        m.input()
        self.__marks.append(m)

    def list_students(self):
        print("\n--- ALL STUDENTS ---")
        for s in self.__students:
            s.list()

    def list_courses(self):
        print("\n--- ALL COURSES ---")
        for c in self.__courses:
            c.list()

    def show_student_mark(self):
        courseid = input("enter course id to get mark: ").strip()
        
        # Tìm thông tin môn học
        selected_course = None
        for c in self.__courses:
            if c.get_idc() == courseid:
                selected_course = c
                break

        if not selected_course:
            print("Course not found!")
            return

        print(f"\n--- MARKS FOR COURSE: {selected_course.get_namec()} ---")
        found = False
        for m in self.__marks:
            if m.get_idc() == courseid:
                # Tìm tên sinh viên tương ứng với ID
                for s in self.__students:
                    if s.get_id() == m.get_id():
                        print(f"Student: {s.get_name()} (ID: {s.get_id()}) | Mark: {m.get_mark()}")
                        found = True
        
        if not found:
            print("No marks recorded for this course.")


# Main Loop
def main():
    app = SchoolManagement()
    while True:
        print("\n--- MENU ---")
        print("1: Input students")
        print("2: Input courses")
        print("3: Input mark")
        print("4: Show all courses")
        print("5: Show all students")
        print("6: Show student mark in course")
        print("7: Exit")
        
        choice = input("choose your option: ").strip()
        
        if choice == '1':
            app.input_student()
        elif choice == '2':
            app.input_courses()
        elif choice == '3':
            app.input_mark()
        elif choice == '4':
            app.list_courses()
        elif choice == '5':
            app.list_students()
        elif choice == '6':
            app.show_student_mark()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()