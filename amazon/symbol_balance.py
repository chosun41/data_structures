def checkSymbolBalance(s):
    
    symbolstack = []
    
    # dictionary to lookup parentheses
    lookup = {'(': ')', '{': '}', '[': ']'}
 
    for c in s:
        if c in lookup:
            symbolstack.append(c)
        elif not symbolstack or lookup[symbolstack.pop()]!=c:
            return False

    return not symbolstack
                    
if __name__ == "__main__":
    
    print(checkSymbolBalance("({)]"))
    print(checkSymbolBalance("{{([][])}()}"))