def hypotenuse(len_a, len_b):
    #the square can be found by multiplying to the power 0.5
    return round((len_a**2 + len_b**2) ** 0.5, 2)
a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))
print("The length of the hypotenuse is" , hypotenuse(a,b))