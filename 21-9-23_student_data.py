class Student:
    def __init__(self):
        self.student_list = []
        self.no_of_students = int(input("Enter number of students:"))
        for _ in range(self.no_of_students):
            name = input("Enter student name: ")
            id = int(input("Enter student id: "))
            grade = input("Enter student grade: ")
            marks1 = int(input("Enter student marks-1: "))
            marks2 = int(input("Enter student marks-2: "))
            marks3 = int(input("Enter student marks-3: "))
            student_info = {
                'name': name,
                'id': id,
                'grade': grade,
                'marks1': marks1,
                'marks2': marks2,
                'marks3': marks3
            }
            self.student_list.append(student_info)

    def save_to_file(self, filename):
        with open(filename, "a+") as student_info:
            for student in self.student_list:
                student_info.write(f"Name: {student['name']}\n")
                student_info.write(f"ID: {student['id']}\n")
                student_info.write(f"Grade: {student['grade']}\n")
                student_info.write(f"Marks-1: {student['marks1']}\n")
                student_info.write(f"Marks-2: {student['marks2']}\n")
                student_info.write(f"Marks-3: {student['marks3']}\n")
                student_info.write("\n")
        print("File is created.")

# Usage
if __name__ == "__main__":
    student_records = Student()
    student_records.save_to_file("D:\\student_info.txt")
