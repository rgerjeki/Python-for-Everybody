hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

pay = 0

if h <= 40:
    #print regular pay
    pay = h * r
else:
    #print overtime pay
    pay = 40 * r 
    h = h - 40
    r = r * 1.5
    pay = pay + h * r

print(pay)