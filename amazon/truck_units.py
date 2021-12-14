def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key = lambda x:x[1],reverse=True)
    count = 0
    num = 0
    for c in boxTypes:
        if num + c[0] <= truckSize:
            count += c[0] * c[1]
            num += c[0]
        elif num < truckSize:
            n = 0
            while n < c[0]:
                if num + 1 <= truckSize:
                    count += 1 * c[1]
                    num += 1
                    n += 1    
                else:
                    break
        else:
            break
    return count

if __name__=='__main__':

    # Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
    # Output: 8
    # Explanation: There are:
    # - 1 box of the first type that contains 3 units.
    # - 2 boxes of the second type that contain 2 units each.
    # - 3 boxes of the third type that contain 1 unit each.
    # You can take all the boxes of the first and second types, and one box of the third type.
    # The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

    print(maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))