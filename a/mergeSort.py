# O(nlogn)

# Don't worry about how this algorithm works, we will cover it later in the course!

def Log_Linear_Example(our_list):
    
    if len(our_list) < 2:
        return our_list
    
    else:
        mid = len(our_list)//2
        left = our_list[:mid]
        right = our_list[mid:]

        Log_Linear_Example(left)
        Log_Linear_Example(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                our_list[k]=left[i]
                i+=1
            else:
                our_list[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            our_list[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            our_list[k]=right[j]
            j+=1
            k+=1
        
        return our_list

print(Log_Linear_Example([56,23,11,90,65,4,35,65,84,12,4,0]))
