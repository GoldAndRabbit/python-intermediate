# Python program to explain property() function
# using property() method


# Alphabet class
class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the value
    def get_value(self):
        return self._value

    # setting the value
    def set_value(self, value):
        self._value = value

    # deleting the value
    def del_value(self):
        print('deleting value')
        del self._value

    '''
    The main purpose of Property() function is to create property of a class.
    By using property() method, we can modify our class and implement the value constraint without any change required to the client code. 
    So that the implementation is backward compatible.
    details see: https://www.geeksforgeeks.org/python-property-function/ 
    
    Syntax: property(fget, fset, fdel, doc)

    Parameters:
    fget() – used to get the value of attribute
    fset() – used to set the value of attribute
    fdel() – used to delete the attribute value
    doc()  – string that contains the documentation (docstring) for the attribute

    Return: Returns a property attribute from the given getter, setter and deleter.
    '''
    value = property(get_value, set_value, del_value)

x = Alphabet('hello')
print(x.value)

x.value = 'nihao'
print(x.value)

del x.value

