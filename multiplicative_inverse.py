def multiplicative_inverse(a, b, t1, t2, t):
    if b == 0:
        return t1
    else:
        rem = a % b
        q = int(a / b)
        t = t1 - t2 * q
        t1 = t2
        t2 = t
        return multiplicative_inverse(b ,rem, t1, t2, t)

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

result = multiplicative_inverse(a, b, 0, 1, 0)
print("The multiplicative inverse of {} and {} is {}".format(a,b,result))