def generate_power_set(input_set):

    res = [[]]
    for input in input_set:
        print(input,res)
        res += [curr + [input] for curr in res]
        print(input,res)

    return res

if __name__ == '__main__':
    
    # time and space: O(n*2^n)
    print(generate_power_set([0,1,2]))