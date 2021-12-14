def knightDialer(n):
    memo, dp = [[4,6],[8,6],[7,9],[4,8],[3,9,0],[],[0,1,7],[2,6],[1,3],[2,4]], [1] * 10
    for i in range(n - 1):
        dp = [sum([dp[j] for j in memo[i]]) for i in range(10)]
    print(dp)
    return sum(dp) % (10 ** 9 + 7)


if __name__ == '__main__':

    # The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

    # A chess knight can move as indicated in the chess diagram below:

    # time and space: O(n)

    print(knightDialer(n = 2))