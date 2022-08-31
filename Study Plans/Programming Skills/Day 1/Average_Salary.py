# QUESTION : You are given an array of unique integers salary where salary[i] is the salary of the ith employee. Return the average salary of employees
#            excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

# Solution :


'''
1) Take List as an input
2) Sort the List
3) Using Slice operator, Slice the list to exclude the first and last element
4) using len() find the length of the list
5) using sum() find the sum of all the elements in the list
6) return the average
'''

class Solution:
    def average(self, salary: List[int]) -> float:
        salary = salary
        salary.sort()
        salary = salary[1:-1]
        length = len(salary)
        added = sum(salary)
        return added/length
