def mincostTickets(days, costs):
    last_day = days[-1]
    days = set(days)
    dp = [0 for _ in range(last_day+1)]
    
    for i in range(1, last_day+1):
        if i not in days:
            dp[i] = dp[i-1]
            continue
        dp[i] = min(dp[max(i-1,0)] + costs[0], 
                    dp[max(i-7, 0)] + costs[1],
                    dp[max(i-30, 0)] + costs[2]
                    )
    print(dp)
    return dp[-1]

if __name__ == '__main__':

    # You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

    # Train tickets are sold in three different ways:

    # a 1-day pass is sold for costs[0] dollars,
    # a 7-day pass is sold for costs[1] dollars, and
    # a 30-day pass is sold for costs[2] dollars.
    # The passes allow that many days of consecutive travel.

    # For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
    # Return the minimum number of dollars you need to travel every day in the given list of days.

    # time and space: O(n)

    print(mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))

    print(mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]))