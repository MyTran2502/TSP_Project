import itertools

def distance(duong_di, matrix):
    cost = 0
    for i in range(len(duong_di) - 1):
        cost += matrix[duong_di[i]][duong_di[i+1]]
    # Quay về thành phố ban đầu
    cost += matrix[duong_di[-1]][duong_di[0]]
    return cost

def tsp_brute_force(matrix):
    so_thanh_pho = len(matrix)
    cac_hoan_vi = itertools.permutations(range(so_thanh_pho))
    
    do_dai_min = float('inf')
    path = None

    for hoan_vi in cac_hoan_vi:
        do_dai = distance(hoan_vi, matrix)
        if do_dai < do_dai_min:     
            do_dai_min = do_dai
            path = hoan_vi

    return path, do_dai_min

