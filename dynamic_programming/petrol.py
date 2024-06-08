MPG=20

def canCompleteTour(gas,cost):

        #sum of gas>= sum cost array
        sum_cost = sum(cost)//MPG
        sum_gas = sum(gas)
        # Check if it is possible to complete the journey
        if sum_cost > sum_gas:
            return -1

        current_gas = 0
        starting_index = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]//MPG
            if current_gas < 0: # only when gas below 0 update gas and starting index
                current_gas = 0
                starting_index = i + 1 
        return starting_index

if __name__ == '__main__':
    
    # time: O(n), space: O(1)
    # return position if you can travel around the circuit once starting from index i station
    # decide whether you can stop there
    
    print(canCompleteTour([50,20,5,30,25,10,10],[900,600,200,400,600,200,100]))
    
    # i,current_gas,starting_indx = 0,50-900/20=5,0
    # i,current_gas,starting_indx = 1,5+20-600/20=-5->0,2
    # i,current_gas,starting_indx = 2,0+5-200/20=-5->0,3
    # i,current_gas,starting_indx = 3,30-400/20=10,3
    # i,current_gas,starting_indx = 4,10 + 25-600/20=5,3  
    # i,current_gas,starting_indx = 5,5 + 10-200/20=5,3  
    # i,current_gas,starting_indx = 5,5 + 10-100/20=10,3 