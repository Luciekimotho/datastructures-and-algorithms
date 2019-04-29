



def twoSum(arr, add):
    n = len(arr)


    for i in arr:
        for j in arr:
            sum = arr[i] + arr[j]
            if sum == add:
                return i, j
            else:
                i += 1
                j += 1

arr = [10, 20, 4, 18, 8]
add = 18

print (twoSum(arr, add))