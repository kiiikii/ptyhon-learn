# Scenario :

	# Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

		# My task is
			# 1 create the variables: john, mary, and adam (v)
			# 2 assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively (v)
			# 3 having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma (v)
			# 4 now create a new variable named totalApples equal to addition of the three former variables (v)
			# 5 print the value stored in totalApples to the console (v)
			# 6 experiment with your code :
				# create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.) (v)
				# Try to print a string and an integer together on one line, e.g., "Total number of apples:" and totalApples ()

#stored var value
john = 3
mary = 5
adam = 6
totalapples = john + mary + adam
minus = john - mary - adam
times = john * mary * adam
divide = john / mary / adam
doudiv = john // mary // adam
doutim = john ** mary ** adam

# driver code
print(john, mary, adam, sep=", ", end="\n\n")
print(totalapples, end="\n\n")
print(minus, end="\n\n")
print(times, end="\n\n")
print(divide, end="\n\n")
print(doudiv, end="\n\n")
print(doutim, end="\n\n")
print("Total number of apples :" and totalapples)