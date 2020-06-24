import sys

def StringCompression(thing):


    curr_char_count = 1
    

    compressed = ""


    for i in range(1, len(thing)):
        if thing[i-1] == thing[i]:
            curr_char_count += 1
        else:
            compressed += str(thing[i-1])
            compressed += str(curr_char_count)
            curr_char_count = 1

    compressed += str(thing[len(thing)-1])
    compressed += str(curr_char_count)
        

    if len(thing) > len(compressed):
        return compressed
    else:
        return thing


    


def main():
    print(StringCompression(sys.argv[1]))

if __name__ == "__main__":
    main()
