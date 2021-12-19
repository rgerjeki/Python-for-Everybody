pay = 0
def computepay(h, r):
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h <= 40:
    pay = h * r
else:
    pay = 40 * r 
    h = h - 40
    r = r * 1.5
    pay = pay + h * r
p = computepay(h, r)
print("Pay", p)