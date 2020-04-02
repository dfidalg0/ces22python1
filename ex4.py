def sum_except_first_even (L):
    s = 0
    found_even = False
    for number in L:
        if not found_even and number % 2 == 1:
            found_even = True
        else:
            s += number

    return s

# Demonstration
def main():
    L = [2,4,11,6,8,10,13]

    x = sum_except_first_even(L)

    print(x)

if __name__ == '__main__':
    main()
