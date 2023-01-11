def sqrt(number):   # https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    start = 0
    end = number
    ans = 1
    while start <= end:
        mid = start + (end - start) // 2

        if mid * mid == number:  # mid is square root
            ans = mid
            break

        elif mid * mid < number:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

