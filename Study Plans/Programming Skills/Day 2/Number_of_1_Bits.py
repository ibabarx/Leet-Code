# QUESTION : Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Solution : 

'''
1 ) Convert the input (dtype = int) to binary using bin()
2 ) convert the binary number to string data type
3 ) using string method  count(), count the number of 1's in the string and return them
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        n = str(n)
        return n.count('1')
        
