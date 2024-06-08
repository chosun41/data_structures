# towers with 3 pegs with largest ring on the bottom, transfer all to another peg but no peg can have 
# ring bigger than the one beneath

NUM_PEGS = 3

def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move,from_peg,to_peg,use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1,from_peg,use_peg,to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg,to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1,use_peg,to_peg,from_peg)

    result = []
    # pegs actually initalized to what it looks like at start on each peg
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result

if __name__ == '__main__':
    
    # time: O(2^n)
    # space: O(n)
    
    # shows all the moves
    x=compute_tower_hanoi(6)
    print(x)
    print(len(x))
    
    y=compute_tower_hanoi(3)
    print(y)
    print(len(y))