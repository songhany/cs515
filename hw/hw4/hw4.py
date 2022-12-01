'''
@author:  Songhan Yu    10470449

CS515 - Hw 4
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
'''

def pascal_row(r):
    '''Input a single integer as row number which will always be an integer greater than or equal to 0. Outputs a list of elements found in a certain row of Pascal’s Triangle'''
    if r == 0:  # base case
        return [1]
    else:
        preRow = pascal_row(r-1)  # subproblem, return previous Row of currentRow. Since if I want to know the final largest pascal row, I need to know the smaller previous row firstly 
        midElementOfCurrentRow = list(map(lambda idx: preRow[idx] + preRow[idx+1], range(len(preRow) -1)))   # len(previous row) - 1 = len(additional mid element in current row). so Except on both sides 1, for the number of mid elment in currentRow is len(preRow) -1
        print(midElementOfCurrentRow)
        return [1] + midElementOfCurrentRow + [1]


def pascal_triangle(n):
    '''Input a single integer n and returns a list of lists containing the values of the all the rows up to and including row n'''
    if n == 0:  # base case
        return [[1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]


def test_pascal_row():
    '''Test pascal_row(r)'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(2) == [1,2,1]
    assert pascal_row(3) == [1,3,3,1]

def test_pascal_triangle():
    '''Test pascal_triangle(n)'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(2) == [[1], [1, 1], [1,2,1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1,2,1], [1,3,3,1]]


# test case
if __name__ == "__main__":
    # test_pascal_row()
    # test_pascal_triangle()
    # print(pascal_row(0))  # [1]
    # print(pascal_row(1))  # [1, 1]
    print(pascal_row(5))  # [1, 5, 10, 10, 5, 1]

    # print(pascal_triangle(0))  # [[1]]
    # print(pascal_triangle(1))  # [[1], [1, 1]]
    # print(pascal_triangle(5))  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]