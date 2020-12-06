class HashTable:
    def __init__(self,size=10,max_load_factor=0.5):
        self.size=size
        self.array=[None]*self.size
        self.max_load_factor=max_load_factor

    def add(self,value):
        
        hash_indx = self.hashfunction(value)
        
        if self.array[hash_indx] is None:
            self.array[hash_indx]=value
        else:
            self.rehash(value)
            
        if len(list(filter(lambda x: x is not None, self.array)))>self.size*self.max_load_factor:
            self.double()
            
    def hashfunction(self,value):
        return value%self.size
    
    def rehash(self,value):
        
        curr_hash_indx = new_hash_indx = self.hashfunction(value)
        
        
#         i=0
#         # linear probing
#         while self.array[new_hash_indx] is not None:
#             new_hash_indx+=1
#             i+=1
           
        #quadratic probing
        i=0
        while self.array[new_hash_indx] is not None:
            new_hash_indx=curr_hash_indx + i**2
            new_hash_indx=self.hashfunction(new_hash_indx)
            i+=1
    
        self.array[new_hash_indx]=value
        
    def double(self):
        
        self.size=len(self.array)*2
        
        new_ht = HashTable(self.size,self.max_load_factor)
        
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            else:
                new_ht.add(self.array[i])
      
        self.array = new_ht.array
        
    def get(self, value):
        curr_hash_indx = new_hash_indx = self.hashfunction(value)
        if self.array[curr_hash_indx] is None:
            raise Exception("key not found") # since it should be the hash or some other hash b/c of collision
        else:
            i=0
            while self.array[new_hash_indx] != value:
                new_hash_indx=curr_hash_indx + i**2
                new_hash_indx=self.hashfunction(new_hash_indx)
                i+=1
            return new_hash_indx,value

if __name__ =='__main__':
    
    # time: O(1) to search
    
    H = HashTable(5,0.5)
    H.add(86)
    H.add(76)
    H.add(16)
    H.add(66)
    H.add(26)
    H.add(21)
    print(H.array)
    print(H.get(21))
