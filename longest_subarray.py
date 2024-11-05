"""
This function takes a binary list of 0's and 1's as input
and aims to find the length of the longest adjacent subarray
with an equal number of 0's and 1's.
"""
def LongestSubarray( array ):
#Assigning a variable to find the maximum length of the longest subarray found
    max_length = 0
#Creating 2 loops, the outer one starts from index 0 in the array to track each index in it
#while the inner one looks at all values from that index to count how many 0's and 1's are avaiable,
#checking if they're equal
    for i in range ( len(array) ):
        sumofzeros = 0
        sumofones = 0
        for j in range( i,len(array) ):
#if condition is needed here to check if the array is empty
            if len (array) == 0:
                max_length = 0
            if array [j] == 0:
                sumofzeros+= 1
            elif array [j] == 1:
                sumofones += 1
            if sumofzeros == sumofones :
#calculate the length of the current subarray
                current_size = j - i + 1
                if current_size > max_length:
                    max_length = current_size
    return max_length

array = [1,0,1,1,0,1]
result = LongestSubarray( array )
print ("The length of the longest adjacent subarray of ",array," is",result)
