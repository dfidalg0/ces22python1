def sum_to (n):
    return n*(n+1)//2

# Demonstration
def main ():
    for i in range(10,100 + 1,10):
        print('From 1 to {}:'.format(i))
        print(sum_to(i))

if __name__ == '__main__':
    main()
