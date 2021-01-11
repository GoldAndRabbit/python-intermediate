
'''
Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts and sets.
The iterator object is initialized using iter() method.
The iterator object use the next() method for iteration.
'''
iterable_value = 'hello'
iterable_obj = iter(iterable_value)
print(iterable_obj)
while True:
    try:
        # iterate by calling next() method
        item = next(iterable_value)
        print(item)
    except StopIteration:
        break

'''
__iter__ method is called for the initialization for an iterator. This returns a iterator object.

__next__ method The next method returns the next value for the iterable. 
When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object which further uses next() method to iterate over. 
This method raises a StopIteration to signal the end of the iteration.
'''
class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x

        if x > self.limit:
            raise StopIteration

        self.x += 1
        return x

# print from 10 to 15
for i in Test(15):
   print(i)

# print nothing
for i in Test(5):
   print(i)

'''
Generators are iterators, but you can only iterate over them once.
It's because they do not store all the values in memory, they generate the values on the fly.
You use them by iterating over them, either with a 'for' loop or by passing them to any function or construct iterates.
Most of the time generators are implemented as functions.
However, they do not return a value, they yield it.
'''

# using generator function
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)

'''
Generators are the best for calculating large sets of results(particularly calculations involving loops themselves) 
where you don't want to allocate the memory for all results at the the same time.
Many Standard Library functions that return lists in Python 2 have been modified to return generators in Python 3, 
because generators require fewer resources
'''

# generator version of calculating fibonacci numbers:
def fibonacci_number(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibonacci_number(100):
    print(x)
