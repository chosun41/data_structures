def maxProfit(prices):
    low, mp = float('inf'), 0
    for p in prices:
        if p < low: 
            low = p
        if p - low > mp: 
            mp = p - low
    return mp
    
if __name__ == '__main__':
    # time: O(n)
    # space: O(1)
    # basically find lowest point and then compare to see if it has max profit
    print(maxProfit([7,1,5,3,6,4]))
    # 6-1=5