def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

result = gcd(int(a), int(b))
print("The GCD of ({},{}) is {}".format(a,b,result))