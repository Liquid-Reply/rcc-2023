def snakesequence(S, m, n):
    sequence = {}
    DP = [[1 for x in range(m+1)] for x in range(n+1)]
    a, b, maximum = 0, 0, 0
    position = [0, 0]
    for i in range(0, n+1):
        for j in range(0, m+1):
            a, b = 0, 0
            p = "initial"
            if(i > 0 and abs(S[i][j] - S[i-1][j]) == 1):
                a = DP[i-1][j]
            if(j > 0 and abs(S[i][j] - S[i][j-1]) == 1):
                b = DP[i][j-1]
            if a != 0 and a >= b:
                p = str(i-1) + " " + str(j)
            elif b != 0:
                p = str(i) + " " + str(j-1)
            q = str(i) + " " + str(j)
            sequence[q] = p
            DP[i][j] = DP[i][j] + max(a, b)
            if DP[i][j] >= maximum:
                maximum = DP[i][j]
                position[0] = i
                position[1] = j
    snakeValues = []
    snakePositions = []
    snakeValues.append(S[position[0]][position[1]])
    check = 'found'
    str_next = str(position[0]) + " " + str(position[1])
    findingIndices = sequence[str_next].split()
    while(check == 'found'):
        if sequence[str_next] == 'initial':
            snakePositions.insert(0, str_next)
            check = 'end'
            continue
        findingIndices = sequence[str_next].split()
        g = int(findingIndices[0])
        h = int(findingIndices[1])
        snakeValues.insert(0, S[g][h])
        snake_position = str(g) + " " + str(h)
        snakePositions.insert(0, str_next)
        str_next = sequence[str_next]
    return [snakeValues, snakePositions]
 
 
S = [[9, 6, 5, 2],
     [8, 7, 6, 5],
     [7, 3, 1, 6],
     [1, 1, 10, 7]]
m = 3
n = 3
seq = snakesequence(S, m, n)
for i in range(len(seq[0])):
    print(seq[0][i], ",", seq[1][i].split())