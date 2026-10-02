from domains.student import Student
from domains.course import Course

def input_students(manager):
    num = int(input("Number of students: "))
    for i in range(num):
        print(f"\n--- Student {i+1} ---")
        s_id = input("Student ID: ").strip()
        name = input("Student Name: ").strip()
        dob = input("DoB (dd/mm/yyyy): ").strip()
        manager.students.append(Student(s_id, name, dob))

def input_courses(manager):
    num = int(input("Number of courses: "))
    for i in range(num):
        print(f"\n--- Course {i+1} ---")
        c_id = input("Course ID: ").strip()
        name = input("Course Name: ").strip()
        credits = int(input("Credits: "))
        manager.courses.append(Course(c_id, name, credits))

def input_marks(manager):
    if not manager.courses or not manager.students:
        print("Please input students and courses first!")
        return

    c_id = input("Enter course ID to input marks: ").strip()
    course_exists = any(c.get_idc() == c_id for c in manager.courses)
    
    if not course_exists:
        print("Course not found!")
        return

    if c_id not in manager.marks:
        manager.marks[c_id] = {}

    print(f"\n--- Entering marks for course {c_id} ---")
    for s in manager.students:
        raw_mark = float(input(f"Mark for {s.get_name()} ({s.get_id()}): "))
        manager.marks[c_id][s.get_id()] = manager.round_down(raw_mark)