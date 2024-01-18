def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    """
    return recursion(num_disks, 'S', 'A', 'D')

def recursion(num_disks, source, auxiliary, destination):
    if num_disks == 0:  # Base condition
        return
    
    if num_disks == 1:  # Termination condition
        print("{} {}".format(source, destination))
        return
        
    '''Just think of one iteration, rest the Recursion will take care!'''
    # Step 1: Move `num_disks - 1` from source to auxiliary
    recursion(num_disks - 1, source, destination, auxiliary)
    
    # Step 2: Now you are left with the only largest disk at source. Move the only leftover disk from source to destination
    print("{} {}".format(source, destination))
    
    # Step 3: Move `num_disks - 1` from auxiliary to destination
    recursion(num_disks - 1, auxiliary, source, destination)


'''
### The Idea
Assume you are writing a function that accepts the following arguments:
        1. arg1 - number of disks
        2. arg2 - rod A - this rod acts as the source (at the time of calling the function)
        2. arg3 - rod B - this rod acts as the auxiliary
        2. arg4 - rod C - this rod acts as the destination
        
Follow the steps below:
1. Given the `num_disks` disks on the source, along with auxiliary and destination rods

2. Check if `num_disks == 1`. This must be the termination condition, therefore use recursion to reach at this moment. 
 - If yes, move disk from source to destination. (Termination condition)

3. For `num_disks > 1`, just think of your FIRST set of steps. You want to pick the bottom most disk on the source, to be transferred to the destination. For this reason, you will will perform the steps below:
 - Step 1: Move `num_disks - 1` from source to auxiliary

 - Step 2: Now you are left with only the largest disk at source. Move the only leftover disk from source to destination
 
 - Step 3: You had `num_disks - 1` disks available on the auxiliary, as a result of Step 1. Move `num_disks - 1` from auxiliary to destination
'''
