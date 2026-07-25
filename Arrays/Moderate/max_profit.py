def max_profit(nums):
    min_price=nums[0]
    max_profit=0
    for price in nums:
        min_price=min(min_price,price)
        profit=price-min_price
        max_profit=max(max_profit,profit)
    return max_profit
print(max_profit([7,1,5,3,6,4]))   # 5
print(max_profit([7,6,4,3,1]))     # 0
print(max_profit([2,4,1]))         # 2
print(max_profit([1,2]))           # 1
print(max_profit([2,1]))           # 0