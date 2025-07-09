import time
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from TSP.algorithms.tsp_brute import tsp_brute_force
from TSP.algorithms.tsp_nn import tsp_nearest_neighbor
from TSP.algorithms.tsp_sa import tsp_simulated_annealing
from TSP.algorithms.tsp_ga import tsp_genetic_algorithm
from TSP.ui.plot import ve_do_thi

def run_gui():
    matrix_cache = []

    def chay():
        nonlocal matrix_cache
        try:
            if not matrix_cache:
                n = int(so_tp.get())
                dong = ma_tran.get("1.0", tk.END).strip().split("\n")
                matrix = [list(map(int, dong[i].split())) for i in range(n)]
                if any(len(row) != n for row in matrix):
                    raise ValueError("Ma trận phải là hình vuông n x n")
                matrix_cache = matrix
            else:
                matrix = matrix_cache
            
            ten_thuat_toan = lua_chon.get()
            start = time.time()
            if ten_thuat_toan == "Brute Force":
                path, dist = tsp_brute_force(matrix)
            elif ten_thuat_toan == "Nearest Neighbor":
                path, dist = tsp_nearest_neighbor(matrix)
            elif ten_thuat_toan == "Simulated Annealing":
                path, dist = tsp_simulated_annealing(matrix)
            elif ten_thuat_toan == "Genetic Algorithm":
                path, dist = tsp_genetic_algorithm(matrix)
            else:
                raise ValueError("Vui lòng chọn một thuật toán hợp lệ.")

            end = time.time()
            thoi_gian = end - start
            duong_di = list(path) + [path[0]]
            ve_do_thi(path, matrix, ten_thuat_toan, dist, duong_di, thoi_gian)

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def reset():
        nonlocal matrix_cache
        matrix_cache.clear()
        so_tp.delete(0, tk.END)
        ma_tran.delete("1.0", tk.END)
        
    #Sinh ma trận ngẫu nhiên 
    def ma_tran_ngau_nhien():
        try:
            n = int(so_tp.get())
            if n <= 1:
                raise ValueError("Số thành phố phải lớn hơn 1")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số thành phố hợp lệ.")
            return

        min_dist = 1
        max_dist = 50
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(0)
                else:
                    row.append(random.randint(min_dist, max_dist))
            matrix.append(row)

        # Hiển thị lên Text widget
        ma_tran.delete("1.0", tk.END)
        for row in matrix:
            row_str = ' '.join(str(x) for x in row)
            ma_tran.insert(tk.END, row_str + "\n")

        matrix_cache.clear()

    # Giao diện
    root = tk.Tk()
    root.title("Giải bài toán TSP")
    root.geometry("520x600")
    root.resizable(True, True)

    ttk.Label(root, text="Nhập vào số thành phố:").grid(row=0, column=0, padx=10, pady=5)
    so_tp = ttk.Entry(root)
    so_tp.grid(row=1, column=0, padx=10, pady=5)

    ttk.Label(root, text="Ma trận khoảng cách (n x n):").grid(row=5, column=0, columnspan=2, padx=10, pady=5)
    ma_tran = tk.Text(root, height=20, width=60)
    ma_tran.grid(row=6, column=0, columnspan=2, rowspan=5, padx=10, pady=5)

    ttk.Label(root, text="Chọn thuật toán:").grid(row=0, column=1, padx=10, pady=5)
    lua_chon = ttk.Combobox(root, values=[
        "Brute Force", "Nearest Neighbor", "Simulated Annealing", "Genetic Algorithm"
    ], state="readonly")
    lua_chon.grid(row=1, column=1, padx=10, pady=5)
    lua_chon.current(0)

    ttk.Button(root, text="Tìm đường đi ngắn nhất", command=chay).grid(row=4, column=0, columnspan=2, pady=10, padx=10)
    ttk.Button(root, text="Nhập lại", command=reset).grid(row=3, column=0, columnspan=2, pady=5, padx=10)
    ttk.Button(root, text="Sinh ma trận ngẫu nhiên", command=ma_tran_ngau_nhien).grid(row=2, column=0, columnspan=2, pady=5, padx=10)

    root.mainloop()
