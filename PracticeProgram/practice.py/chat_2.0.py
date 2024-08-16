# Find the Missing Number: Given a list of integers from 1 to n (inclusive) with one element missing, find the missing number.
# Example: For the list [1, 2, 4, 6, 3, 7, 8], the missing number is 5.

def find_num(list):
    num=0
    while True :
        num=num+1
        if num not in list :
            return num
        
print('The missing number in the list is : ', find_num([1,2,3,4,5,7,8,6,10]))

# Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring without repeating characters.
# Example: For the input "abcabcbb", the longest substring without repeating characters is "abc" with a length of 3.

def longest_sub_String(String):
    l=[]
    for alphabet in String:
        if alphabet not in l :
            l.append(alphabet)
        else :
            String = ''.join(i for i in l)
            return (String , len(String)) 
        
print('The longest sub String is ',longest_sub_String( "abcabcbb"))

# Rotate Image: Given an n x n matrix representing an image, rotate the image by 90 degrees (clockwise) in place.

# def rotate(matrix):
#     # Suppose the matrix is 3 *3 : 
#     matrix_90=[]
#     for outer_index in matrix(reversed):
#         for num in outer_index:

i=[1,2,3,4,5]

for j in i(reversed):
    print(j)