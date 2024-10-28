""" --------------------------------------------------------------------

Split function

    => divide a string into a list of strings based on a specified separator
    
"""

name = "ryan zafft"
namelist = name.split(" ")
print(namelist)
print(f"First Name : {namelist[0]}")
print(f"Last Name : {namelist[1]}")


names = "ryan|nile|kim"
namelist = names.split("|")
print(namelist)

equation = "1+2+4+10+5"
numbers = equation.split("+")
print(equation)


""" --------------------------------------------------------------------

Modulo Operator

    => finds the remainder of a division operation between two numbers
    => x%y tells us the remainder of x when it is divided by y
    => if we want to check if x is divisible by y we can check if x%y == 0
    
"""

print(100%10)

print(100%7)

print(25%5)

print(25%3)


""" --------------------------------------------------------------------

USER INPUT

    => requires use of the command line 
    
    => give user the ability to change the value of variables while the program is running
    
    => uses the 'Input()' function
    
    => every input returns a string. thus if you want to ask the user for a number as input
       you must first get the input (as a string) then convert it to a number

    
"""

# geting strings as input is straightfoward and easy
name = input("Enter your name : ")
print(type(name))
print(name)

# geting integers, decimals, and other numeric values requires some more thinking

# example 1 : what is wrong?
# answer : if we dont input a integer, the conversion will fail
age = int(input("Enter your age : "))
print(type(age))
print(age)

# example 2 : what is wrong?
# answer : nothing, this is how we want to handle integer inputs
age = input("Enter your age : ")
print(type(age))
if age.isdigit():
    age=int(age)
    print(age)
else:
    print(f"We cannot conver {age} to an integer!")
print(type(age))

""" --------------------------------------------------------------------

WHILE LOOPS 

    => For Loops Vs. While Loops
        - For loops run for a finite number of iterations. THEY CANNOT BE INFINTE LOOPS
        - While loops can also do this, but they allow for more flexability. 
        - While loops are not constrained to run only for a set number of iterations, 
          but instead, they run WHILE a condition is true. Because of this, 
          while loops CAN BE INFINITE LOOPS, because they dont stop until a condition is met, 
          and if that condition is never met, then they keep on running
          
    => While loops repeat all the code inside the loop until a defined condition is met
    
    => While loops terminate in two ways:
        (1) The condition in the while statement evaluates to false
        (2) A 'break' statement inside the while loop is executed
        
    => Examples
            
            while(True):
                if (some statement):
                    break
                    
            running = True
            while(running):
                if (some statement):
                    running = False
                    
            i = 0
            while (i < 10):
                i+=1
"""

########################################################################   
# EXAMPLE 1 : finding the average of a list of numbers with a while loop  
########################################################################   

testscores = [67, 75, 81, 85, 84, 90, 92, 88, 75, 77, 91, 92, 73, 98, 89]

# Find the average of the test scores using a for loop
sum_testscores = 0
for i in range(len(testscores)):
    sum_testscores += testscores[i]
print(f"The average score is {sum_testscores/len(testscores)}")

# Find the average of the test scores using a for loop (METHOD 1)
sum_testscores = 0
i = 0
while(i < len(testscores)):
    sum_testscores += testscores[i]
    i+=1
print(f"The average score is {sum_testscores/len(testscores)}")

# Find the average of the test scores using a for loop (METHOD 2)
sum_testscores = 0
i = 0
while(True):
    if i >= len(testscores):
        break
    sum_testscores += testscores[i]
    i+=1
print(f"The average score is {sum_testscores/len(testscores)}")
    
########################################################################   
# EXAMPLE 2 : while loop with user input  
######################################################################## 

name = ""
while(name != "ryan"):
    name = input("Enter your name : ")
    
names = []
user_input = ""
while (True):
    user_input = input("Enter some names seperated by commas : ")
    if (user_input == 'exit'):
        break
    newnames = user_input.split(',')
    for name in newnames:
        names.append(name)
    print(names)

    
