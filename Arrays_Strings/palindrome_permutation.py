# Simple solution 
# type in True or False for case sensitivity
# can take in space-separated words("taco cat")

import sys

def palindrome_permutation(case_sensitive, palindrome):

    input = ""

    for i in palindrome:
        input += i

    if not case_sensitive:
        input = input.lower()

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
    print(palindrome_permutation(bool(sys.argv[1]),sys.argv[2:]))



if __name__ == "__main__":
    main()