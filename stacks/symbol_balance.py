from stack import Stack

def checkSymbolBalance(s):
    
    symbolstack = Stack()
    
    # dictionary to lookup parentheses
    lookup = {'(': ')', '{': '}', '[': ']'}
    
    # for each character
    # if in lookup keys, then push on stack
    # if it is every empty or poped element doesn't match lookup value, then return false
    for c in s:

        if c in lookup:
            symbolstack.push(c)
        elif symbolstack.isEmpty() or lookup[symbolstack.pop()] != c:
            # Unmatched right char or mismatched chars.
            return False
        
    # if you reached the end and the stack is empty, then it is balanced
    return symbolstack.isEmpty()
                    
if __name__ == "__main__":
    
    print(checkSymbolBalance("({)]"))
    print(checkSymbolBalance("{{([][])}()}"))