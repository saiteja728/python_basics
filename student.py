def StudentData():
        student_name=input("enter student name")
        sub1=int(input("enter subject1 marks"))
        sub2 = int(input("enter subject2 marks"))
        sub3 = int(input("enter subject3 marks"))
        return student_name,sub1,sub2,sub3

def GradeCheck(sub1,sub2,sub3):
        total=sub1+sub2+sub3
        per=total/3
        if per >= 75 and sub1 >= 60 and sub2 >= 60 and sub3 >= 60:
            return "Distinction"
        elif sub1 >= 60 and sub2 >= 60 and sub3 >= 60:
            return "First Class"
        elif sub1 >= 50 and sub2 >= 50 and sub3 >= 50:
            return "Second Class"
        elif sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
            return "Third Class"
        else:
            return "Fail"

student_no_of_records = 0
while student_no_of_records < 3:
    student_name, sub1, sub2, sub3 = StudentData()
    grade = GradeCheck(sub1, sub2, sub3)

    print("Student name:", student_name)
    print("Grade:", grade)

    add_records = input("Do you want to enter another record? (Y/N): ")

    if add_records.upper() == "Y":
        student_no_of_records += 1
    else:
        break

