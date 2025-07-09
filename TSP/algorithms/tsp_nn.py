def tsp_nearest_neighbor(matrix, start=0):
    n = len(matrix)
    visited = [False] * n
    path = [start]
    visited[start] = True
    total_cost = 0
    current = start

    for _ in range(n - 1):
        next_city = None
        min_distance = float('inf')

        for j in range(n):
            if not visited[j] and 0 < matrix[current][j] < min_distance:
                min_distance = matrix[current][j]
                next_city = j

        path.append(next_city)
        visited[next_city] = True
        total_cost += min_distance
        current = next_city

    # Quay lại điểm xuất phát
    total_cost += matrix[current][start]

    return path, total_cost
