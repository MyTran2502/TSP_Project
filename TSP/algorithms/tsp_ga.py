import random

def distance(duong_di, matrix):
    cost = 0
    for i in range(len(duong_di) - 1):
        cost += matrix[duong_di[i]][duong_di[i + 1]]
    # Quay về thành phố ban đầu
    cost += matrix[duong_di[-1]][duong_di[0]]  
    return cost

def tao_ca_the(n):
    ca_the = list(range(1, n))
    random.shuffle(ca_the)
    return [0]+ca_the

def tao_quan_the(kich_thuoc_quan_the, n):
    quan_the=[]
    for _ in range(kich_thuoc_quan_the):
        quan_the.append(tao_ca_the(n))
    return quan_the

def lai_ghép(cha1, cha2):
    size = len(cha1)
    start, end = sorted(random.sample(range(1, size), 2))
    con = [None] * size
    con[0] = 0
    con[start:end+1] = cha1[start:end+1]

    chi_so = (end + 1) % size
    if chi_so==0: chi_so=1
    for gen in cha2:
        if gen not in con:
            while con[chi_so] is not None:
                chi_so = (chi_so + 1) % size
            con[chi_so] = gen
    return con

def dot_bien(ca_the, ti_le_dot_bien=0.05):
    if random.random() < ti_le_dot_bien:
        i, j = random.sample(range(1, len(ca_the)), 2)
        ca_the[i], ca_the[j] = ca_the[j], ca_the[i]

def chon_loc(quan_the, matrix, so_luong):
    quan_the.sort(key=lambda ca_the: distance(ca_the, matrix))
    return quan_the[:so_luong]

def tsp_genetic_algorithm(matrix, so_the_he=500, kich_thuoc_quan_the=100, ti_le_dot_bien=0.05):
    n = len(matrix)
    quan_the = tao_quan_the(kich_thuoc_quan_the, n)
    path = min(quan_the, key=lambda ca_the: distance(ca_the, matrix))

    for the_he in range(so_the_he):
        quan_the_moi = []
        quan_the_chon = chon_loc(quan_the, matrix, kich_thuoc_quan_the // 2)

        while len(quan_the_moi) < kich_thuoc_quan_the:
            cha1, cha2 = random.sample(quan_the_chon, 2)
            con = lai_ghép(cha1, cha2)
            dot_bien(con, ti_le_dot_bien)
            quan_the_moi.append(con)

        quan_the = quan_the_moi
        ca_the_tot = min(quan_the, key=lambda ca_the: distance(ca_the, matrix))
        if distance(ca_the_tot, matrix) < distance (path, matrix):
         path = ca_the_tot

    do_dai_min = distance (path, matrix)
    return path, do_dai_min
