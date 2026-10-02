def list_courses(manager):
    print("\n=== COURSE LIST ===")
    for c in manager.courses:
        c.list()

def list_students(manager):
    print("\n=== STUDENT LIST (SORTED BY GPA DESCENDING) ===")
    manager.sort_students_by_gpa()
    for s in manager.students:
        s.list()

def show_marks(manager):
    c_id = input("Enter course ID: ").strip()
    if c_id in manager.marks:
        print(f"\n=== MARKS FOR COURSE: {c_id} ===")
        for s in manager.students:
            mark = manager.marks[c_id].get(s.get_id(), "N/A")
            print(f"Student: {s.get_name():<20} (ID: {s.get_id():<8}) -> Mark: {mark}")
    else:
        print("No marks recorded for this course.")