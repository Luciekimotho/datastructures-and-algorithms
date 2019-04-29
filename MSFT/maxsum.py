#Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of 
#numbers which has the largest sum. 


def MaxSum(arr):
    maxSoFar = maxEndingHere = 0
    start = 0
    end = 0
    s = 0

    if len(arr) == 0 :
        raise ValueError("Invalid input")
    elif len(arr) == 1:
        return arr
    else:
        for i in range(0, len(arr)):
            maxEndingHere += arr[i]
            
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
                print (arr[i])

            if maxEndingHere < 0:
                maxEndingHere = 0
                #print (arr[i])

        return maxSoFar

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print (MaxSum(arr))