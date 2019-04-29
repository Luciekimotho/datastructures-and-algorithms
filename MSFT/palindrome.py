#Integer Palindrome with a twist
#Most numbers can be made into palindromes by taking the original number, reversing the digits, then adding the original number to the reversed digits. 
#If that number isn’t a palindrome, then repeat the same process until you reach a palindrome.
#if the number becomes larger than 1,000,000 and still doesn’t form a palindrome, then return false

#TEBOW IT 
#what is the input?
#invalid inputs? strings? null? negative numbers?
#what should we return? true/ false
#what if original number is palindrome

#case               example         output
#one digit input      4               yes
#same digit number   444              yes
#palindrome already  121              yes
#boundary           1000000           no
#can never be a palindrome ??         no
#good case          1234

#reverse num                                                   is_palindrome(num):
#if original == rev                                                if num == rev(num):
#    is_palindrome                                                     return true
#else                                                              else: 
#    original += reverse                                               while (num <= 1,000,000):
#check is_palindrome while original <= 1,000,000                            num += rev(num)
#                                                                           is_palindrome(num)

def reverse(num):
    rev = 0
    while num != 0:
        rev = rev*10 + num%10
        num //= 10
    return rev

#using recursion
def check_palindrome(num):
    if num == reverse(num):
        return True
    while num <= 1000000:
        num += reverse(num)
        if check_palindrome(num):
            return True
        return False

print(reverse(4))
print(check_palindrome(90089))


#without recursion
#returns True if is palindrome & False if not
def is_palindrome(num, rev):
    return num == rev

def make_palindrome(num):
    while num <= 1000000:
        if is_palindrome(num, reverse(num)):
            return True
        else:
            num += reverse(num)
    return False

print(make_palindrome(90089))