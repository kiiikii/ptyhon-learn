# Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y
# My task is to complete the code in order to evaluate the following expression: 3x^3 - 2x^2 + 3x - 1
# The result should be assigned to y
# -----------------------------
	# Remember that classical algebraic notation likes to omit the multiplication operator - you need to use it explicitly
	# Note how we change data type to make sure that x is of type float
	#--------------------------------------------------
		# Keep your code clean and readable, and test it using the data we've provided, each time assigning it to the x variable (by hardcoding it)
		# Don't be discouraged by any initial failures. Be persistent and inquisitive
x = -1
x2 = 1
x3 = 0

xs = float(x)
xs2 = float(x2)
xs3 = float(x3)

# write your code here
y = 3*(xs**3) - 2*(xs**2) + 3 * xs - 1
y1 = 3*(xs2**3) - 2*(xs2**2) + 3 * xs2 - 1
y2 = 3*(xs3**3) - 2*(xs3**2) + 3 * xs3 - 1

print("y =", y, end="\n")
print("y =", y1, end="\n")
print("y =", y2, end="\n")