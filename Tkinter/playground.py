# # Args
def add(*args):
    sum = 0
    for n in args:
        sum +=n
    print(sum)
    
add(1,2,3,4,5,6,7,8,9,10)

# kwargs
def calculate(**kwargs):
    for key,value in kwargs.items():
        print(value)
        print(key)

calculate(add=3,multiply=5)

def calculation(a, *args, **kwargs):
    sum = 0
    for n in args:
        sum += n
        sum +=kwargs["add"]
        sum +=kwargs["multiply"]
    print(sum)
    
calculation(2, 2, 3, 4, add=3,multiply=5)

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        # use .get if it doesn't find it it outputs None
        self.age = kwargs.get("age")
        self.gender = kwargs.get("gender")
        
person = Person(name = "Alice", gender = 'F')
print(person.age)
print(person.name)

