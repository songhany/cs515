# below method below store 2 result of subproblem. STORE AS MUCH AS RESULT POSSIBLE
memo1 = {}
def fibN1(n):
    if n in memo1:
        return memo1[n]
    if n < 0:
        return 'Incorrect Input'
    elif n == 0:
        memo1[n] = 0
        return 0
    elif n == 1 or n == 2:
        memo1[n] = 1
        return 1
    else:
        first_iterm =  fibN1(n-1) 
        memo1[n-1] = first_iterm
        second_iterm = fibN1(n-2)
        memo1[n-2] = second_iterm
        return first_iterm + second_iterm

print(fibN1(5))


memo = {}
def fibN(n):
    if n in memo:
        return memo[n]
    if n < 0:
        return 'Incorrect Input'
    elif n == 0:
        memo[n] = 0
        return 0
    elif n == 1 or n == 2:
        memo[n] = 1
        return 1
    else:
        result = fibN(n-1) + fibN(n-2)
        memo[n] = result  # this just store one result
        return result

print(fibN(5))


