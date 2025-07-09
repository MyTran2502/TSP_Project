import random
import math

def distance(path, matrix):
    cost = 0
    for i in range(len(path)):
        cost += matrix[path[i]][path[(i + 1) % len(path)]]
    return cost

def tsp_simulated_annealing(matrix, initial_temp=1000, cooling_rate=0.995, stopping_temp=1e-8, max_loop=1000):
    n = len(matrix)
    current_path = list(range(1, n))
    random.shuffle(current_path)
    current_path = [0] + current_path
    current_cost = distance(current_path, matrix)

    duong_di_tot_nhat = list(current_path)
    do_dai_min = current_cost

    temp = initial_temp
    loop_count = 0

    while temp > stopping_temp and loop_count < max_loop:
        # Sinh lời giải hàng xóm bằng cách hoán đổi 2 thành phố
        i, j = random.sample(range(1, n), 2)
        new_path = list(current_path)
        new_path[i], new_path[j] = new_path[j], new_path[i]
        neighbor_cost = distance(new_path, matrix)

        # Chấp nhận lời giải mới theo xác suất SA
        delta = neighbor_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_path = new_path
            current_cost = neighbor_cost

            # Cập nhật lời giải tốt nhất
            if current_cost < do_dai_min:
                duong_di_tot_nhat = current_path
                do_dai_min = current_cost

        temp *= cooling_rate
        loop_count += 1

    return duong_di_tot_nhat, do_dai_min
