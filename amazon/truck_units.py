def maximumUnits(boxTypes, truckSize):
    
    boxTypes.sort(key = lambda x: x[1],reverse=True)
    num_units=0
    num_boxes=0

    for box in boxTypes:
        
        if num_boxes + box[0]<=truckSize:
            num_units += box[0]*box[1]
            num_boxes += box[0]
        elif num_boxes<truckSize:
            curr_num_boxes = box[0]
            print(curr_num_boxes)

            while curr_num_boxes>0 and num_boxes<truckSize:
                num_units += box[1]
                num_boxes +=1
                curr_num_boxes-=1
        else:
            break

    return num_units

if __name__=='__main__':

    # Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
    # Output: 8
    # Explanation: There are:
    # - 1 box of the first type that contains 3 units.
    # - 2 boxes of the second type that contain 2 units each.
    # - 3 boxes of the third type that contain 1 unit each.
    # You can take all the boxes of the first and second types, and one box of the third type.
    # The total num_boxesber of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

    print(maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))