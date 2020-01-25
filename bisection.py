def func(x):
    return x * x * x + x -3

def bisection(a, b):
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    while ((b - a) >= 0.0001):

        c = (a + b) / 2

        if (func(c) == 0.0):
            break

        if (func(c) * func(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is : ", "%.8f" % c)

a = 1
b = 3
bisection(a, b) 