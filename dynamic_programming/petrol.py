MPG=20

def canCompleteTour(petrol, cost):
    minVal = float("inf")
    minPos = -1
    petrolTillNow = 0
    for i in range(1, len(petrol)+1):
        petrolTillNow += petrol[i-1] - cost[i-1]//MPG
        if petrolTillNow < minVal:
            minVal = petrolTillNow
            minPos = i
    return minPos

if __name__ == '__main__':
    
    # time: O(n), space: O(1)
    # return position if you can travel around the circuit once starting from index i station
    
    print(canCompleteTour([50,20,5,30,25,10,10],[900,600,200,400,600,200,100]))
    
    # gallons left - [5,-10,-5,10,-5,0,5]

    # minval=inf,minpos=01,petrolTillNow=0
    # i=1,petrolTillNow=0+5=5,minval=5,minpos=0
    # i=2,petrolTillNow=5-10=-5,minval=-5,minpos=1
    # i=3,petrolTillNow=-5-5=-10,minval=-10,minpos=2
    # i=4,petrolTillNow=-10+10=0,minval=-10,minpos=2
    # i=5,petrolTillNow=-5,minval=-10,minpos=2
    # i=6,petrolTillNow=-5,minval=-10,minpos=2
    # i=7,petrolTillNow=0,minval=-10,minpos=2