# input
a = eval(input("Input A value: "))
b = eval(input("Input B value: "))
c = eval(input("Input C value: "))
d = eval(input("Input D value: "))
r = eval(input("Input R value: "))

# function
formula = ((((r + 34) * 3)/4) - (9 * (a + (b * c))) + ((3 + (d * (2 + a)) / (a + (b * d)))))

print("The answer is: " + str(formula))