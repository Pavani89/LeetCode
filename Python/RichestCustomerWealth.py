'''
1672.You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
'''

# Time complexity: O(m*n)
# Space complexity: O(1)

def maximum_wealth(accounts):
    max_wealth = 0
    for customer in accounts:
        # print(f"customer:  {customer}")
        wealth = sum(customer)
        max_wealth = max(max_wealth, wealth)
    return max_wealth

# Testing the function
input = [[1,2,3],[3,2,1]]
print(maximum_wealth(input))

input2=[[1,5],[7,3],[3,5]]
print(maximum_wealth(input2))

input3=[[2,8,7],[7,1,3],[1,9,5]]
print(maximum_wealth(input3))