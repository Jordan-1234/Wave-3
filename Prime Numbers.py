def primefactors(n):
    if n < 2: 
        print("Cannot be factored")
    else: 
        factor = 2
        while factor <= n:
            if n % factor == 0:
                print(factor)
                n /= factor
            else:
                factor += 1

n = int(input("Enter a number (2 or greater): "))
print("The prime factors of", n, "are: ")
primefactors(n)