import matplotlib.pyplot as plt
import networkx as nx

def ve_do_thi(path, matrix, ten_thuat_toan, dist, duong_di, thoi_gian):
    G = nx.DiGraph()
    n = len(matrix)

    for i in range(n):
        G.add_node(i)

    for i in range(n):
        a = path[i]
        b = path[(i + 1) % n]  # quay lại điểm đầu
        G.add_edge(a, b, weight=matrix[a][b])

    # Vị trí node theo vòng tròn
    pos = nx.circular_layout(G)
    plt.figure(num=f"{ten_thuat_toan}")
    plt.title(f"Đường đi ngắn nhất: {duong_di}\nTổng độ dài: {dist}\nThời gian chạy: {thoi_gian:.8f}s")

    # Vẽ các node và cạnh
    nx.draw(G, pos, arrows=True, with_labels=True, node_color='lightblue', node_size=800, edge_color='red', width=2)

    # Hiển thị trọng số
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.tight_layout()
    plt.show()
