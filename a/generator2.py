# A valid sudoku square satisfies these two properties:
#   1. Each column of the square contains each of the whole numbers from 1 to n exactly once.
#   2. Each row of the square contains each of the whole numbers from 1 to n exactly once.

from tabnanny import check
from numpy import square


correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
def check_sudoku(sodoku):

    for row in sodoku:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(sodoku[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)


    for j in range(len(sodoku[0])):
        check_list = list(range(1, len(sodoku[0]) + 1))
        for row in sodoku:
            if row[j] not in check_list:
                return False
            check_list.remove(row[j])

    return True 

    
#print(check_sudoku(incorrect))
#>>> False

#print(check_sudoku(correct))
#>>> True

#print(check_sudoku(incorrect2))
#>>> False

#print(check_sudoku(incorrect3))
#>>> False

#print(check_sudoku(incorrect4))
#>>> False

#print(check_sudoku(incorrect5))
#>>> False

