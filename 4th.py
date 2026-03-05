def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_palindrome(num) and is_prime(num):
    print(f"{num} is both a palindrome and a prime number.")
else:
    print(f"{num} is NOT both a palindrome and a prime number.")
