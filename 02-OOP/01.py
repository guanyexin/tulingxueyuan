class Student():
    pass

class PythonStudent():
    name = None
    age = 18
    course = "python"
    def doHomework(self):
        print("I love doing my honmework")
        return None

xiaowang = PythonStudent()
print(xiaowang.name)
print(xiaowang.course)
xiaowang.doHomework()