class Person:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last

    def asleep(self, time):
        return 0 <= time <= 7

    def __str__(self):
        return self.firstName + " " + self.lastName

    def __eq__(self, other: object) -> bool:
        return self.firstName == other.firstName \
            and self.lastName == other.lastName


class Student:
    def __init__(self, first, last, gpa) -> None:
        Person.__init__(self, first, last)
        self.gpa = gpa
    
    def asleep(self, time):
        return 3 <= time <= 11
    
    def __str__(self) -> str:
        return Person.__str__(self) + ", " + " GPA=" +  str(self.gpa)


class SITstudent(Student):
    def __init__(self, first, last):
        Student.__init__(self, first, last, 0)
        self.grades = []
    
    def __str__(self):
        return Person.__str__(self)

    def status(self, time):
        if self.asleep(time):
            return str(self) + " is asleep now."
        return str(self) + " is gaming or studying."

    def addGrade(self, score):
        self.grades += [score]
        self.gpa = sum(self.grades) / len(self.grades)        

    def getGrades(self):
        return self.grades


someone = SITstudent("Jean", "Zu")
print(someone.status(10))

alice = SITstudent("Alice", "Cleverness")
alice.addGrade (70)
alice.addGrade (80)
print ("Alice’s grades " + str(alice.getGrades()))
agrad = alice.getGrades()
agrad[0] = 100      # this will change alice grades list (easy make MISTAKE)
print("Alice’s grades now " + str(alice.getGrades()))
# SOLUTION
# Alice ’s grades [70, 80]
# Alice ’s grades now [100, 80]