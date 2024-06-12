
print("This is a Fibonacci Generator")
print("Each Fibonacci number will be displayed as 'Fibonacci [Index]: Number'")
print("How many terms do you want to have? (Counting the zero)")
terms = int(input("# of terms:"))

Fibonacci = [0, 1]

num1 = 0
num2 = 1

for i in range(0, terms):
    num3 = num1 + num2
    Fibonacci.append(num3)
    num1 = num2
    num2 = num3
    print("Fibonacci [", i, "]: ", Fibonacci[i])
