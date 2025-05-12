class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

class Course:
    def __init__(self,course_name):
        self.course_name = course_name 
        self.students = []

    def add_students(self,students):
        self.students.append(students)

    def course_average(self):
        count = 0
        for student in self.students:
            count += student.marks

        print(count/len(self.students))


student1 = Student("John", 20, 85)
student2 = Student("Jane", 22, 90)
student3 = Student("Doe", 21, 78)

course1 = Course("Mathematics")

course1.add_students(student1)
course1.add_students(student2)
course1.add_students(student3)

course1.course_average()




