from stack import Stack

def isPalindrome(str):
    
    strStack = Stack()
    palindrome = True
     
    for char in str:
        strStack.push(char)
         
    for char in str:
        if char == strStack.pop():
            continue
        else:
            return False
             
    return palindrome
 
if __name__ == "__main__":
    
    # just push onto stack and pop to check against string
    print(isPalindrome("madam"))
    print(isPalindrome("mds"))