# class Parent:
#     def __init__(self, name='sai', id=101, phone=4555566):
#         self.name = name
#         self.id = id
#         self.phone = phone
#
# class Child(Parent):
#     def __init__(self, name, id, phone, age=34, mail="tejas59@gmail.com"):
#         super().__init__(name, id, phone)
#         self.age = age
#         self.mail = mail
#
#     def display(self):
#         print("Name:", self.name)
#         print("ID:", self.id)
#         print("Phone:", self.phone)
#         print("Age:", self.age)
#         print("Mail:", self.mail)
#
# childObj = Child("teja", 102, 1234567)
# childObj.display()
class Calculator:
    def add(self, a=None, b=None, c=None):
        if b is None:
            return a
        elif c is None:
            return a + b
        elif a is None and b is None and c is None:
            print("no value is given give some values")
        else:
            return a + b + c

calc = Calculator()

result1 = calc.add(5)
result2 = calc.add(5, 10)
result3 = calc.add(5, 10, 15)
result4 =  calc.add()

print(result1)
print(result2)
print(result3)
print(result4)

