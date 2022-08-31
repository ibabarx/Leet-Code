# QUESTION : Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# SOLUTION : 

'''
*   If N is even then the count of both odd and even numbers will be N/2.
*   If N is odd, 
      - If L or R is odd, then the count of the odd numbers will be N/2 + 1, and even numbers  = N – countofOdd.
      - Else, the count of odd numbers will be N/2 and even numbers = N – countofOdd.
    
    SOURCE : https://www.geeksforgeeks.org/count-odd-and-even-numbers-in-a-range-from-l-to-r/
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high-low+1) % 2 == 0:
            return (high-low+1) // 2
        elif (high-low+1) % 2 == 1:
            if low%2==1 or high%2==1:
                return ((high-low+1) // 2)+1
            else:
                return (high-low+1) // 2
            
            
            
        
