def count_words_up_to_sam (L):
    s = 0
    for word in L:
        if type(word) == str:
            s += 1
        if word == 'sam':
            break
    return s

# Demonstration
def main():
    L = ['abc','def','ghi','sam', 'pop','bob','gel']

    x = count_words_up_to_sam(L)

    print(x)

if __name__ == '__main__':
    main()
