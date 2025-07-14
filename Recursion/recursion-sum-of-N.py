def sum_of_N_numbers(i, n, sum):
    if i > n:
        return sum
    sum += i
    return sum_of_N_numbers(i+1, n, sum)

n = int(input("Enter a number: "))
total = sum_of_N_numbers(1, n, 0)
print(total)