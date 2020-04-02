def sum_up_to_first_even (L):
    s = 0
    for number in L:
        if number % 2 == 1:
            break
        s += number

    return s

# Demonstration
def main():
    L = [2,4,11,6,8,10,13]

    x = sum_up_to_first_even(L)

    print(x)

if __name__ == '__main__':
    main()
