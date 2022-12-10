def get_alphabet(number):
    """
    Helper function to figure out alphabet of a particular number
    Remember: 
        * ASCII for lower case 'a' = 97
        * chr(num) returns ASCII character for a number e.g. chr(65) ==> 'A'
    """
    # return chr(number + 96)
    return chr(number + ord('a') - 1)


def all_codes(number):
    if number == 0:
        return [""]

    # 1. calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    alphabet = get_alphabet(remainder)
    output_100 = list()


    if number > 9 and remainder <= 26:
        output_100 = all_codes(number // 100)  # get all codes for the remaining number


        for idx, element in enumerate(output_100):
            output_100[idx] = element + alphabet


    # 2. calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10
    alphabet = get_alphabet(remainder)

    output_10 = all_codes(number // 10)  # get all codes for the remaining number


    for idx, element in enumerate(output_10):
        output_10[idx] = element + alphabet


    output = list()
    output.extend(output_100)
    output.extend(output_10)

    return output


if __name__ == "__main__":
    # print(get_alphabet(1))
    print(all_codes(26))
    print(all_codes(27))
    print(all_codes(123))
    print(all_codes(145))
    print(all_codes(1145))
    print(all_codes(4545))