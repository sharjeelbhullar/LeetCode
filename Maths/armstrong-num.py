from math import log10
def armstrong_num(n):
    power = int(log10(n)+1)
    dup = n
    sum = 0
    while n > 0:
        last_digit = n % 10
        sum += last_digit ** power
        n //= 10
    
    if sum == dup:
        return "Armstrong"
    else:
        return "Not Armstrong"
    
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(armstrong_num(n))