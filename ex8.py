def print_table (n):
    print('     ', end = '')

    for i in range(1,n+1):
        print('{:4d}'.format(i), end = '')
    print()

    print('  :--' + '----' * n)

    for i in range(1,n+1):
        print('{:2d}:'.format(i), end = '  ')
        for j in range(1,n+1):
            print('{:4d}'.format(i*j), end = '')
        print()

# Demonstration
def main ():
    print_table(12)

if __name__ == '__main__':
    main()
