def complex_sum (a,b):
    return (a[0] + b[0], a[1] + b[1])

# Demonstration
def main ():
    from random import random

    a = (random(), random())
    b = (random(), random())

    s1 = complex(*a) + complex(*b)

    s2 = complex_sum(a,b)
    s2 = complex(*s2)

    try:
        assert s1 == s2
    except AssertionError:
        print('Something went wrong')
    else:
        print('Program running properly')

if __name__ == '__main__':
    main ()
