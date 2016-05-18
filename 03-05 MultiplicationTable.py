number = raw_input("Enter a number : ")
number = int(number)

for i in range(10):
    print str(number) + " x " + str(i + 1) + " = " + str(number * (i + 1))
