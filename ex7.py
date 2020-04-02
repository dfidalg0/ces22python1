def sum_of_squares (xs):
    s = 0
    for x in xs:
        s += x**2

    return s

# Demonstration
def main ():
    for i in range(5,10 + 1):
        L = list(range(1,i+1)) # Generate list [1,2,3,...,i]
        print('Sum of 1 + 4 + 9 + ... + {}:'.format(i**2))
        print(sum_of_squares(L))

if __name__ == '__main__':
    main()
