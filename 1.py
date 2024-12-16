class Student:
    def __init__(self, name, age, national_number, student_number, GPA):
        self.name = name
        self.age = age
        self.national_number = national_number
        self.student_number = student_number
        self.GPA = GPA
    
    def get_first_name(self):
        return "Name: " + self.name
    
    def get_age(self):
        return self.name + " is " + str(self.age) + " years old"
    
    def get_GPA(self):  
        return self.name + " has a GPA of " + str(self.GPA)
    
    def get_national_number(self):  
        return self.name + "'s national number is " + str(self.national_number)


student_1 = Student('Danial Soufi', 22, 2121040709020, 1870701151, 17)
student_2 = Student('Media Sharifi', 23, 2121040709035, 3750621802, 18)
student_3 = Student('Arvin Zaheri', 22, 2121040709029, 375061140, 19)


print(student_1.get_first_name())
print(student_1.get_age())
print(student_1.get_GPA())
print(student_1.get_national_number())
