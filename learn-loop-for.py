# for loops within range (10)
for i in range(10):
    print("The value of i is currently", i)
    pass

print("")

# for loops with range (2, 8)
for i in range(2, 8):
    print("The value of i is currently", i)

print("")

# More about the for loop and the range() function with three arguments
for i in range(2, 8, 3):
    print("The value of i is currently", i)

print("")

# more about the for loop and the range function with power
pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2 