# Scenario
# -----------
    # Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
    # The results have to be printed to the console.
    # You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.
    # Test your code - does it produce the results you expect?
    # We won't show you any test data - that would be too simple.

# input a float value for variable a here
side1 = float(input("length side 1 : "))
# input a float value for variable b here
side2 = int(input("length side 2 : "))

# Drive Code
# -------------
# output the result of addition here
print("the result of addition : " + str(side1 + side2 + side1 + side2), end="\n\n")
# output the result of subtraction here
print("the result of subtraction : " + str(side1 - side2), end="\n\n")
# output the result of multiplication here
print("the result of multiplication : " + str(side1 * side2), end="\n\n")
# output the result of division here
print("the result of division : " + str(side1 / side2), end="\n\n")
print("That's all, folks!")