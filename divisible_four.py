for numbers in range (0, 100):
    if (numbers % 4 <= 0):
        print ("divisible by four")
        
        while numbers % 4 <= 0:
            numbers = numbers + 1
            print(numbers)
        
               