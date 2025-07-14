num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num //= 10
print("Reversed num is:", reverse)