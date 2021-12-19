hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
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