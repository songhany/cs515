def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""

def keypad(num):
    output = list()
    
    if num == 0:
        return [""]
    
    rightDigit = num % 10
    rest_num = num // 10
    
    sub_output = keypad(rest_num)
    
    for curChar in get_characters(rightDigit):
        for aheadChar in sub_output:
            new_string = aheadChar + curChar
            output.append(new_string)
    
    return output 


def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")


print(keypad(0))
input = 0
expected_output = [""]
test_keypad(input, expected_output)


print(keypad(23))
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
test_keypad(input, expected_output)


print(keypad(32))
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)


print(keypad(8))
input = 8
expected_output = sorted(["t", "u", "v"])
test_keypad(input, expected_output)


print(keypad(354))
input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)



def keypad_solution(num):
    if num <= 1:
        return [""]
    elif 1 < num <= 9:
        return list(get_characters(num))
    
    last_digit = num % 10
    sub_output = keypad_solution(num // 10)

    keypad_string = get_characters(last_digit)
    output = list()

    for curChar in keypad_string:
        for aheadChar in sub_output:
            new_string = aheadChar + curChar
            output.append(new_string)

    return output
