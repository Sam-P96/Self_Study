# class experiment

class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

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


s1 = Student("Sam", 29, 100)

print(type(s1))
print(s1.get_name())
print(s1.get_age())
s1.a_noise()
s1.a_function("trucks", "buildings")

