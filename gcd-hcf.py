num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
gcd = 0
for i in range(1, min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD =", gcd)


# optimize approach
while num1 > 0 and num2 > 0:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1
    
if num1 == 0:
    print(num2)
print(num1)