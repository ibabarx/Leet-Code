# QUESTION : Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# Solution : 

'''
1 ) Using list comprehension, create a list of digits in the number after converting each number to string data type.
2 ) Using map() , convert each digit in the list from String Data type to Int data type.
3 ) Using sum(),  add  all the elements of the list, and put it into add variable.
4 ) using prod(), from the math library, multiply all the elements in the list and add it to mul variable.
5 ) return  (mul - add)
'''

import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [digit for digit in str(n)]
        nums = list(map(int, nums))
        add = sum(nums)
        mul = math.prod(nums)
        return (mul - add)
