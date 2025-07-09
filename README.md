## MÔ PHỎNG VÀ ĐÁNH GIÁ CÁC THUẬT TOÁN ĐỂ GIẢI BÀI TOÁN NGƯỜI BÁN HÀNG (TSP)

# Mô tả dự án
Dự án này nhằm mục đích:
- Mô phỏng quá trình giải TSP bằng các thuật toán Brute Force, Nearest Neighbor, Genetic Algorithm và Simulated Annealing
- Triển khai và đánh giá hiệu quả (thời gian thực thi, tổng độ dài hành trình) của từng thuật toán
<!--  -->
# Cấu trúc thư mục
tsp_source/
    ├──main.py                          <!--Tập tin khởi chạy chính  -->
    ├──README.md 
    └──TSP/                        
        ├── algorithms/
        │   ├── tsp_brute.py            <!--Thuật toán Brute Force  -->
        │   ├── tsp_nn.py               <!--Thuật toán Nearest Neighbor  -->
        │   ├── tsp_ga.py               <!--Thuật toán Genetic Algorithm -->
        │   ├── tsp_sa.py               <!--Thuật toán Simulated Annealing  -->
        └── ui/
            ├── gui.py                  <!--Giao diện người dùng  -->
            └── plot.py                 <!--Vẽ đồ thị hành trình  -->                   


# Các thư viện sử dụng
- tkinter                               <!--Giao diện người dùng-->
- matplotlib                            <!--Vẽ đồ thị kết quả-->
- networkx                              <!--Tạo và hiển thị đồ thị tuyến đường-->
- randomn itertools, math, time         <!--các thư viện chuẩn của python-->

# Hướng dẫn chạy chương trình
- Yêu cầu: Python 3.x
- Cài đặt thư viện cần thiết matplotlib và networkx:
             pip install matplotlib networkx
- Chạy chương trình trong Terminal (Windows): 
             python main.py

# Tác giả
- Trần Thảo My - B2204947
- Đại học Cần Thơ - Trường Công Nghệ Thông Tin & Truyền Thông
- Niên luận cơ sở ngành Mạng máy tính & Truyền thông dữ liệu
- Email: myb2204947@student.ctu.edu.vn

