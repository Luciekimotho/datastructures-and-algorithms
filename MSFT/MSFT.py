
#reverse

def reverse(word):
    rev = ""
    for char in word:
        rev = char + rev
    return rev


def sen(input_str):
    upp_str = input_str.upper()
    return upp_str[::-1]


#Remove duplicates from a given string
#input_str("geeksforgeeks")
#output_str("geeksfor")
def removeDups(str):
    unique_str = ''
    for char in str:
        if char not in unique_str:
            unique_str += char
    return unique_str

#Given a string str, the task is to print all the sub-sequences of str.
def maximumSum(arr):
    maxSum = 0
    length = len(arr) - 1
    
    for i in range(length):
        sum = arr[i] + arr[i+1]
        if sum > maxSum:	
            maxSum = sum
            q = i
            p = i+1

    print(arr[q])
    print(arr[p])
    return maxSum
    

#first split the sentence into an arr of words
words = "He is a boy".split() 
#print (words)

#declare an array to hold the reversed words
revWords = []

#loop through words while reversing each word
for word in words:
    rev = reverse(word)
    revWords.append(rev)
#print (revWords)


#revStr = (" ").join(revWords)
#print (revStr)
#print(sen("good boy"))

#print(removeDups("geeksfor"))

arr = [18, 4, 7, 3, 17, 12, 3, 10]
print(maximumSum(arr))