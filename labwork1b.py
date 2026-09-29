students = []
courses = []
mark = []
#list students' information
def input_student():
    numberS = int(input('number of students:'))
    for i in range(numberS):
        id = int(input('student id:'))
        name = input('name of students:')
        dob = input('date of birth:(xx/yy/zzzz)')
        students.append({'id':id,'name':name,'dob':dob})

#get courses' information
def input_courses():
    numberC = int(input('courses:'))
    for i in range(numberC):
        idc = int(input('id courses:'))
        namec = input('name courses:')
        courses.append({'idc':idc , 'namec':namec})

#get marks of students
def input_mark():
    mark1 = float(input('enter your mark:'))
    id = int(input('student id:'))
    idc = int(input('id courses:'))
    mark.append({'id':id, 'idc':idc ,'mark':mark1})

#show courses' information
def list_courses():
    for listcourse in courses:
        print(f'all information of courses: {listcourse['idc']} and {listcourse['namec']}')

#show students' information
def list_students():
    for liststudent in students:
        print(f'all information of students: {liststudent['id']} and  {liststudent['name']}')

#show students' marks
def show_student_mark():
  courseid = input('enter course id to get mark:')
  for mark1 in mark:
      liststudent = [i for i in students if i['id'] == mark1['mark']]
      listcourse = [i for i in courses if i['idc'] == mark1['mark']]
      if liststudent and listcourse:
       print(f'student: {liststudent['name']}, course:{liststudent['namec']} and mark:{mark1['mark']}')

#options 
while True:
    print('menu\n',
  '---1:name student---\n','---2:name course---\n','---3:mark---\n','---4:all course---\n','---5:show student---\n','---6:show student mark in course:---\n','---7:exit---\n')
    random1 = input('choose your information:')
    if random1 == '1':
        input_student()
    elif random1 == '2':
        input_courses()
    elif random1 == '3':
        input_mark()
    elif random1 == '4':
        list_courses()
    elif random1 == '5':
         list_students()
    elif random1 == '6':
          show_student_mark()
    break 
else:
 print('exit')
    