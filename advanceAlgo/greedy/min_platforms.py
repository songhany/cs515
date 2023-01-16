def min_platforms(arrival, departure):
    if(len(arrival) != len(departure)): # Mismatch in the length of the lists
        return -1

    arrival.sort()
    departure.sort()

    platform_required = 1
    max_platform_required = 1

    i = 1
    j = 0

    while i < len(arrival) and j < len(arrival):
        if arrival[i] < departure[j]:
            platform_required += 1
            i += 1

            if platform_required > max_platform_required:
                max_platform_required = platform_required

        else:
            platform_required -= 1
            j += 1

    return max_platform_required


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)