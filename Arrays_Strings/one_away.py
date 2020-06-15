# Problem:
# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character.
# Given 2 strings, check if they are one or less edits away



import sys

def OneAway(s1, s2):

    string_diff = abs(len(s1) - len(s2))

    if string_diff > 1:
        return False

    edit_count = 0

    insert = False
    delete = False

    index1 = 0
    index2 = 0

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            edit_count +=1 

            if edit_count > 1:
                return False

            if len(s1) > len(s2):
                index1+=1
            elif len(s2) > len(s1):
                index2+=1
        index1+=1
        index2+=1

    return True


                

    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            # insert
            if s2[i+1] == s1[i]:
                edit_count += 1
                insert = True
            # delete
            elif s1[i+1] == s2[i]:
                edit_count +=1
                delete = True
            # replace
            else:
                edit_count +=1
        elif insert:
            if s2[i+1] != s1[i]:
                return False
        elif delete:
            if s1[i+1] != s2[i]:
                return false
        if edit_count > 1:
            return False
        
    if edit_count == 1 and string_diff > 1:
        return False

    return True




def main():
    print(OneAway(sys.argv[1], sys.argv[2]))



if __name__ == "__main__":
    main()