# Scenario
# ------------------
# Your task is to complete the code in order to evaluate the following expression:
    # 1 / x + 1 / x + 1 / x + 1 / x

x = float(input("Enter value for x: "))
# put your code here
y = round((x ** 3) + (2 * x)) / ((x ** 4) + (3 * x ** 2) + 1)

print("y =", y)