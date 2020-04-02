def is_palindrome (string):
    return string == ''.join(reversed(string))

# Demonstration
def main ():
    try:
        assert is_palindrome('abba')
        assert not is_palindrome('abab')
        assert is_palindrome('tenet')
        assert not is_palindrome('banana')
        assert is_palindrome('straw warts')
        assert is_palindrome('a')
    except AssertionError:
        print('Something went wrong')
    else:
        print('Program working properly')

if __name__ == '__main__':
    main()
