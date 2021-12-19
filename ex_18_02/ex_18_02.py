largest = None
smallest = None
y = True
yes_no = ""


def Ext(x):
    x = input("Would you like to enter another number? ('y', 'n'): ")
    
    if x == "y": #continues while loop
        y = True
    elif x == "n":
        print("Maximum is", largest) #output largest number
        print("Minimum is", smallest) #output smalles number
        exit() #closes program
    else: #input has to be 'y' or 'n'
        print("Invalid Input")
        Ext(x)

while y == True:
    try:
        num = int(input("Enter a number in between (-100 -> 1000): ")) #enter numbers
    except ValueError: #prints invalid if input is not int value
        print("Invalid Input")
        continue
    if num > 1000 or num < -100: #setting input boundries
        print("Invalid Input") #prints invalid if not within boundries
        continue
      
    for value in range(-101, num): #allows numbers below 0 to be read
        if smallest == None and largest == None: #starting numbers added to smallest and largest
            smallest = num
            largest = num
        elif num < smallest: #makes numbers following first number smallest if num < smallest
            smallest = num
        elif num > largest: #makes numbers following first number largest if num > largest
            largest = num 
    
    Ext(yes_no) #calls Ext function
    

    