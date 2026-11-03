def calculate_largest_rectangle(heights):

    indx=[]
    max_area=0
    for i,h in enumerate(heights + [0]): # !!! dont forget [0]
        while indx and heights[indx[-1]]>=h:
            height = heights[indx.pop()] # !!! height is from pop, not separate
            width= i if not indx else i - indx[-1]-1
            max_area=max(max_area,height*width)
        indx.append(i)
    return max_area

    # basically pop indx until you get to a height which is not less than current height
    # calculate max area with each pop, extending back to last entry in indx

if __name__ == '__main__':
    
    # O(n)
    # heights of building, find max area of rectangle under the skyline
    print(calculate_largest_rectangle([1,4,2,5,6,3,2,6,6,5,2,1,3]))
    
    # i,h,indx,max_area = 0,1,[],0          
    # i,h,indx,max_area = 0,1,[0],0
    
    # i,h,indx,max_area = 0,1,[0],0         
    # i,h,indx,max_area = 1,4,[0,1],0   
     
    # i,h,indx,max_area = 1,4,[0,1],0       
    # i,h,indx,max_area = 2,2,[0],4*(2-0-1)=4   
    # indx = [0,2]

    # i,h,indx,max_area = 2,2,[0,2],4    
    # i,h,indx,max_area = 3,5,[0,2,3],4   

    # i,h,indx,max_area = 3,5,[0,2,3],4  
    # i,h,indx,max_area = 4,6,[0,2,3,4],4  

    # i,h,indx,max_area = 4,6,[0,2,3,4],4
    # i,h,indx,max_area = 5,3,[0,2,3],6*(5-3-1)=6
    # i,h,indx,max_area = 5,3,[0,2],5*(5-2-1)=10
    # i,h,indx,max_area = 5,3,[0,2,5],10

    # i,h,indx,max_area = 5,3,[0,2,5],10
    # i,h,indx,max_area = 6,2,[0,2],3*(6-2-1)=9<10
    # i,h,indx,max_area = 6,2,[0],2*(6-0-1)=10
    # i,h,indx,max_area = 6,2,[0,6],10

    # i,h,indx,max_area = 6,2,[0,6],10
    # i,h,indx,max_area = 7,6,[0,6,7],10

    # i,h,indx,max_area = 7,6,[0,6,7],10
    # i,h,indx,max_area = 8,6,[0,6,7,8],10

    # i,h,indx,max_area = 8,6,[0,6,7,8],10
    # i,h,indx,max_area = 9,5,[0,6,7],6*(9-7-1)=6<10
    # i,h,indx,max_area = 9,5,[0,6],6*(9-6-1)=6<2=12
    # i,h,indx,max_area = 9,5,[0,6,9],12

    # i,h,indx,max_area = 9,5,[0,6,9],12
    # i,h,indx,max_area = 10,2,[0,6],5*(10-6-1)=15
    # i,h,indx,max_area = 10,2,[0],2*(10-0-1)=18
    # i,h,indx,max_area = 10,2,[0,10],18

    # i,h,indx,max_area = 10,2,[0,10],18
    # i,h,indx,max_area = 11,1,[0],2*(11-0-1)=20
    # i,h,indx,max_area = 11,1,[0,11],20
    
    # i,h,indx,max_area = 11,1,[0,11],20
    # i,h,indx,max_area = 12,3,[0,11,12],20

