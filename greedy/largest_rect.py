def calculate_largest_rectangle(heights):

    indx=[]
    max_area=0
    for i,h in enumerate(A + [0]):
        while indx and A[indx[-1]]>=h:
            height= A[indx.pop()]
            width= i if not indx else i - indx[-1]-1
            max_area=max(max_area,height*width)
        indx.append(i)
    return max_area

if __name__ == '__main__':
    
    # O(n)
    # heights of building, find max area of rectangle under the skyline
    print(calculate_largest_rectangle([1,4,2,5,6,3,2,6,6,5,2,1,3]))
    
    # i=0,h=1,pillar_indices=[0]
    # i=1,h=4,pillar_indices=[0,1]
    # i=2,h=2,4>=2,pillar_indices=[0],height=4,width=2-0-1=1,max_area=4,1<2,pillar_indices=[0,2]
    # i=3,h=5,2<5,pillar_indices=[0,2,3]
    # i=4,h=6,5<6,pillar_indices=[0,2,3,4]
    # i=5,h=3,6>=3,pillar_indices=[0,2,3],height=6,width=5-3-1=1,max_area=6,5>=3,pillar_indices=[0,2],height=5,width=5-2-1=2,max_area=10
    # 2<3,pillar_indices=[0,2,5]
    # i=6,h=2,3>=2,pillar_indices=[0,2],height=3,width=6-2-1=3,max_area=10,2>=2,pillar_indices=[0],height=2,width=6-0-1=5,max_area=10,1<2
    # pillar_indices=[0,6]
    # i=7,h=6,2<6,pillar_indices=[0,6,7]
    # i=8,h=6,6>=6,pillar_indices=[0,6],height=6,width=8-6-1=1,max_area=10,2<6,pillar_indices=[0,6,8]
    # i=9,h=5,6>=5,pillar_indices=[0,6],height=6,width=9-6-1=2,max_area=12,2<5,pillar_indices=[0,6,9]
    # i=10,h=2,5>=2,pillar_indices=[0,6],height=5,width=10-6-1=3,max_area=15,2>=2,pillar_indices=[0],height=2,width=10-0-1=9,max_area=18,
    # 1<2,pillar_indices=[0,10]
    # i=11,h=1,2>=1,pillar_indices=[0],height=2,width=11-0-1=10,max_area=20,1>=1,pillar_indices=[],height=1,width=11,max_area=20,
    # pillar_indices=[11]
    # i=12,h=3,1<3,pillar_indices=[11,12]
    # i=13,h=0,3>=0,pillar_indices=[11],height=3,width=13-11-1=1,max_area=20,1>=0,height=1,width=13,max_area=20,pillar_indices=[13]
