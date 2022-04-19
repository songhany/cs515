'''
Demonstration of Python's 'name mangling' which is a
little like 'private' in other languages. Python does
not have private variables.
'''

class Person:
    def __init__(self, first, last):
        self.firstName = first
        self.__lastName = last # note two underscores

    def __str__(self):
        return self.firstName + " " + self.__lastName

    def __eq__(self,other):
        return self.firstName == other.firstName \
               and self.__lastName == other.__lastName

# The following code is _not_ inside the class.

a = Person("Ada", "Lovelace")
b = Person("Anita", "Borg")  
print(a.firstName)         # prints Ada
a.firstName = "First"
a.__lastName = "Programmer" 
print(a)                   # prints First Lovelace
print(a._Person__lastName) # prints Lovelace
print(a.__lastName)        # prints Programmer 


# An attribute like __lastName which starts with two
# underscores gets converted to a longer name of this
# form: _Person__lastName.

# Main points: Code outside a class should not directly access
# the attributes of that class; better to use getters and setters.
# Name mangling helps prevent writing bad code, by making it a
# little harder to directly access the attributes.

