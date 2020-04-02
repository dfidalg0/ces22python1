from math import sqrt

def is_prime (n):
    N = int(sqrt(n))
    for i in range(2,N + 1):
        if n % i == 0:
            return False
    else:
        return True

# Demonstration
def main ():
    try:
        assert is_prime(11)
        assert not is_prime(35)
        assert is_prime(19911121)
        assert not is_prime(9)
    except AssertionError:
        print('Something went wrong')
    else:
        print('Program working properly')

if __name__ == '__main__':
    main()
