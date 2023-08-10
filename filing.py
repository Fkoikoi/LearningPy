import dict1

def invert_dict(d):
    inverse = dict()
    for key in d:
        for val in d[key]:
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
                return inverse
                
# Taking "dict1.py" as input file
# in reading mode
with open("dict1.py", "r") as input:
      
    # Creating "dict1.py" as output
    # file in write mode
    with open("dict1.py", "w") as output:
          
        # Writing each line from input file to
        # output file using loop
        for line in input:
            output.write(line)
