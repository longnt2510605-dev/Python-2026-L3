from domains.mark_manager import MarkManager
import input as in_mod
import output as out_mod

def main():
    manager = MarkManager()
    while True:
        print("\n" + "="*30)
        print(" STUDENT MANAGEMENT SYSTEM (PW4) ")
        print("="*30)
        print("1. Input Students")
        print("2. Input Courses")
        print("3. Input Marks")
        print("4. List Courses")
        print("5. List Students (Sorted by GPA)")
        print("6. Show Marks")
        print("0. Exit")
        
        choice = input("Choose option: ").strip()
        if choice == '1': in_mod.input_students(manager)
        elif choice == '2': in_mod.input_courses(manager)
        elif choice == '3': in_mod.input_marks(manager)
        elif choice == '4': out_mod.list_courses(manager)
        elif choice == '5': out_mod.list_students(manager)
        elif choice == '6': out_mod.show_marks(manager)
        elif choice == '0':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()