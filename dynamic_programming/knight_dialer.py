def knightDialer(n):
    
    memo, res = [[4,6],[6,8],[7,9],[8,4],[0,3,9],[],[1,7,0],[2,6],[1,3],[2,4]],[1]*10
    for i in range(1,n):
        res = [sum(res[j] for j in x) for x in memo ]
    print(res)
    return sum(res) % (10 ** 9 + 7)
if __name__ == '__main__':

    # 1 2 3
    # 4 5 6
    # 7 8 9
    # # 0 *

    # The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

    # A chess knight can move as indicated in the chess diagram below:

    # time and space: O(n)

    print(knightDialer(n = 2))