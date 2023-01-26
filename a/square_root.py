def squareRoot(number, precision):   # https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/
 
    if number < 0:
        return str(squareRoot(-number, precision)) + 'i'

    start = 0
    end, ans = number, 1
 
    # For computing integral part
    # of square root of number
    while (start <= end):
        mid = int((start + end) / 2)
 
        if (mid * mid == number):
            ans = mid
            break
 
        # incrementing start if integral
        # part lies on right side of the mid
        if (mid * mid < number):
            start = mid + 1
            ans = mid
 
        # decrementing end if integral part
        # lies on the left side of the mid
        else:
            end = mid - 1
 
    # For computing the fractional part
    # of square root upto given precision
    increment = 0.1
    for i in range(0, precision):
        while (ans * ans <= number):
            ans += increment
 
        # loop terminates when ans * ans > number
        ans = ans - increment
        increment = increment / 10
 
    return ans


print(round(squareRoot(50, 3), 4))
print(round(squareRoot(10, 4), 4))
print(squareRoot(27, 8))
print(squareRoot(-4, 0))


# edge1
print ("Pass" if  (0 == squareRoot(0, 0)) else "Fail")

# edge2
print ("Pass" if  ('2i' == squareRoot(-4, 0)) else "Fail")

# edge3
print ("Pass" if  (4294967296 == squareRoot(pow(2, 64), 0)) else "Fail")
