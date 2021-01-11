# Python program to explain property() function
# using @property decorator


# Alphabet class
class Alphabet:
    def __init__(self, value):
        self._value = value

    '''
    The property decorator turns value() method into a getter for a read-only attribute with the same name.
    details see: https://www.geeksforgeeks.org/python-property-function/ 
    '''
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.deleter
    def value(self):
        del self._value

x = Alphabet('cristiano')
print(x.value)

x.value = 'messi'
print(x.value)

del x.value
