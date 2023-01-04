def case_sort(string):
    upperCharIdx = 0
    lowerCharIdx = 0
    sortedString = sorted(string)

    for idx, char in enumerate(sortedString):
        ascii_int = ord(char)
        if 97 <= ascii_int <= 122:   # ASCII value of a = 97 & ASCII value of z = 122
            lowerCharIdx = idx
            break
            
    output = list()
    for char in string:
        ascii_int = ord(char)
        if 97 <= ascii_int <= 122:
            output.append(sortedString[lowerCharIdx])
            lowerCharIdx += 1
        else:
            output.append(sortedString[upperCharIdx])
            upperCharIdx += 1
    return "".join(output)