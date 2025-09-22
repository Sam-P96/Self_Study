# class experiment
from collections.abc import async_generator


class Dog:
    def __init__(self, name, breed, noise: str):
        self.name = name
        self.breed = breed
        self.noise = noise

    def make_noise(self):
        print(self.noise * 3)

class Student:
    created = 0
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.created = Student.created + 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def a_noise(self):
        print(f"{self.get_name()} says: Hello!")

    def a_function(self, str1: str, str2: str) -> None:
        """
        Prints a sentence stating what the student can juggle and eat
        :param str1: item to be juggled
        :param str2: item to be eaten
        :return: `student` can juggle `item 1` and eat `item 2`!
        """
        output = f"{self.get_name()} can juggle {str1} and eat {str2}!"
        print(output)

class Course:
    def __init__(self,name , max_student):
        self.name = name
        self.max_student = max_student
        self.student_list = []

    def get_name(self):
        return self.name

    def get_list(self):
        return self.student_list

    def add_student(self, new_student):
        if len(self.student_list) < self.max_student:
            self.student_list.append(new_student.get_name())
            print(f"{new_student.get_name()} added.")
        else:
            print(f"Not enough space in the '{self.get_name()}' course"
                  f" to add {new_student.get_name()}.")

d1 = Dog("Ashura", "Golden Retriever", "龍雅は敵を食らう！！")

d1.make_noise()

s1 = Student("Sam", 29, 95)
s2 = Student("Mary", 22, 97)
s3 = Student("Kelvin", 11, 75)
# print(type(s1))
print(s1.get_name())
print(s1.get_age())
s1.a_noise()
s1.a_function("trucks", "buildings")
print(f"{Student.created} students have been created!")

c1 = Course("Don't Be Suspicious", 2)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
print(f"Current students in the course: {c1.get_list()}")