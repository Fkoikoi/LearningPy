new_students = {"names": ["freena", "ruben", "bill"],"teachers": ["richard", "john", "paul"],"color": ["red", "white", "blue"]}

def invert_dict(d):
    inverse = dict()
    for key in d:
        for val in d[key]:
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
                return inverse
        
def my_dict():
    inverted_dict = invert_dict(new_students)
    print('the original dict:', new_students)
    print('the inverted one:', inverted_dict)
        
        
my_dict()