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
    def __init__(self, first, last, age) -> None:
        Person.__init__(self, first, last)
        self.age = age
    
    def asleep(self, time):
        return 3 <= time <= 11
    
    def __str__(self) -> str:
        return Person.__str__(self) + ", asleep is " + str(self.asleep(4))


class Duck(Student):
    def __init__(self, first, last, age, dorm) -> None:
        Student.__init__(self, first, last, age)
        self.dorm = dorm
    
    def asleep(self, time):
        return super().asleep(time)


d = Duck("songhan", "yu", 18, "Washington Street")
print(d)
print(d.asleep(5))