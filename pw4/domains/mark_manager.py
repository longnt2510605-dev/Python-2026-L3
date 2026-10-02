import math
import numpy as np

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {} # {course_id: {student_id: mark}}

    def round_down(self, mark):
        return math.floor(mark * 10) / 10.0

    def calculate_gpa(self, student_id):
        marks_list = []
        credits_list = []

        for course in self.courses:
            c_id = course.get_idc()
            if c_id in self.marks and student_id in self.marks[c_id]:
                marks_list.append(self.marks[c_id][student_id])
                credits_list.append(course.get_credits())

        if not credits_list:
            return 0.0

        np_marks = np.array(marks_list)
        np_credits = np.array(credits_list)
        
        gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
        return self.round_down(gpa)

    def sort_students_by_gpa(self):
        for s in self.students:
            s.set_gpa(self.calculate_gpa(s.get_id()))

        if not self.students:
            return

        gpas = np.array([s.get_gpa() for s in self.students])
        sort_indices = np.argsort(gpas)[::-1]
        self.students = [self.students[i] for i in sort_indices]