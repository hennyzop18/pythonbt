maximum = int(input(" Please Enter the Maximum Value : "))
total = 0

for number in range (1, maximum+1) :
    if (number % 2 !=0) :
        print("(0".format(number))
        total += number
        
print("The sum of Even numbers from 1 to (0) = {1} ".format(number,total))
