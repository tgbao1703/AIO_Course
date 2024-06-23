from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

class Ward:
    def __init__(self, name: str):
        self._name = name
        self.__people = []

    def add_person(self, person: Person):
        self.__people.append(person)

    def describe(self):

        print(f"Ward Name: {self._name}")

        for person in self.__people:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.__people if isinstance(person, Doctor))

    def sort_age(self):
        self.__people.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        teachers = [person for person in self.__people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        return sum(teacher.get_yob() for teacher in teachers) / len(teachers)

# init objects
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

# create ward and add person
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

# describe ward
ward1.describe()

# count doctor
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# sort by age
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# compute average age of teachers
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")