import sys

def palindrome_permutation(input):

    palin_dict = {}

    isOdd = False

    for c in input:
        if c not in palin_dict:
            palin_dict[c] = 1
        else:
            palin_dict[c] += 1

    for key in palin_dict.keys():
        if palin_dict[key] % 2 == 1:
            if isOdd:
                return False
            else:
                isOdd = True
    
    return True

            

def main():
    print(palindrome_permutation(sys.argv[1]))



if __name__ == "__main__":
    main()