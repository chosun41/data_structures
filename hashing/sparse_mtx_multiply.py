def multiply(A, B):
    cols = [[(j, b) for j, b in enumerate(col) if b] for col in zip(*B)] # if b skips over O index
    print(cols) # [col 0 (row idx, val), col1, (row idx, val)]
    return [[sum(row[j]*b for j, b in col) for col in cols] for row in A] # no enumerate here

if __name__=='__main__':
    A = [
          [ 1, 0, 0],
          [-1, 0, 3]]

    B = [
          [ 7, 0, 0 ],
          [ 0, 0, 0 ],
          [ 0, 0, 1 ]]
    print(list(zip(*B)))# turns rows to cols
    print(multiply(A,B))