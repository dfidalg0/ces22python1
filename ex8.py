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
def main (n):
    print_table(n)

if __name__ == '__main__':
    from sys import argv
    n = int(argv[1]) if len(argv) > 1 else 12
    main(n)
