score = input("Enter grade in decimal form: ")
try:
    s = float(score)
except:
    print("Error, please enter numeric input")
    quit()

if s > 1.0:
    print("Error, out of range")
    quit()
elif s < 0.0:
    print("Error, out of range")
    quit()
elif s >= 0.9:
    print("Letter Grade = A")
elif s >= 0.8:
    print("Letter Grade = B")
elif s >= 0.7:
    print("Letter Grade = C")
elif s >= 0.6:
    print("Letter Grade = D")
else:
    print("Letter Grade = F")

