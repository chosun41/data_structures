def gcd(x,y):
    return x if y==0 else gcd(y,x%y)

if __name__ == '__main__':
    
    # time: O(log max(x,y))
    
    print(gcd(27,81))
    print(gcd(81,27))
    print(gcd(7,5))