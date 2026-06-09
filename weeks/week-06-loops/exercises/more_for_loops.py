"""
TỔNG HỢP VÍ DỤ VÒNG LẶP FOR (TỪ CƠ BẢN ĐẾN NÂNG CAO) 🔄
====================================
File này giúp bạn làm quen với for loop qua các ví dụ thực tế, dễ hiểu.
"""

# ==========================================
# P
# ==========================================

# 0.1. Lặp lại một hành động nhiều lần
print("--- 0.1. In một câu chào 3 lần ---")
for i in range(3):
    print("Chào bạn! Chúc bạn học tốt.") # Câu này sẽ in ra 3 lần


# 0.2. Duyệt qua một danh sách đơn giản
print("\n--- 0.2. In danh sách thú cưng ---")
pets = ["Chó", "Mèo", "Thỏ"]
for pet in pets:
    print(f"Nhà mình có nuôi một chú: {pet}")


# 0.3. Tính tổng một dãy số đơn giản
print("\n--- 0.3. Tính tổng từ 1 đến 5 ---")
tong = 0
for so in range(1, 6): # Lấy các số: 1, 2, 3, 4, 5
    tong = tong + so
print(f"Tổng các số từ 1 đến 5 là: {tong}")


# ==========================================
# PHẦN 2: CÁC CÁCH DÙNG LINH HOẠT KHÁC 🚀
# ==========================================

# 1. Duyệt qua một chuỗi (String)
print("\n--- 1. Duyệt qua từng ký tự trong chuỗi ---")
word = "Python"
for char in word:
    print(f"Ký tự: {char}")


# 2. Duyệt qua một Tuple
print("\n--- 2. Duyệt qua các phần tử trong Tuple ---")
colors = ("red", "green", "blue")
for color in colors:
    print(f"Màu sắc: {color}")


# 3. Duyệt qua các khóa (keys) của Dictionary
print("\n--- 3. Duyệt qua các khóa của Dictionary ---")
student_scores = {"An": 8.5, "Bình": 9.0, "Chi": 7.8}
for name in student_scores: # Mặc định duyệt qua keys
    print(f"Tên sinh viên: {name}")


# 4. Duyệt qua các giá trị (values) của Dictionary
print("\n--- 4. Duyệt qua các giá trị của Dictionary ---")
for score in student_scores.values():
    print(f"Điểm số: {score}")


# 5. Duyệt qua cả khóa và giá trị (items) của Dictionary
print("\n--- 5. Duyệt qua cả khóa và giá trị của Dictionary ---")
for name, score in student_scores.items():
    print(f"Sinh viên {name} đạt {score} điểm")


# 6. Vòng lặp FOR với range() và bước nhảy âm (đếm ngược)
print("\n--- 6. Đếm ngược từ 5 về 1 ---")
for i in range(5, 0, -1):
    print(i)


# 7. Vòng lặp lồng nhau (Nested For Loops) - Ví dụ bảng cửu chương
print("\n--- 7. Bảng cửu chương từ 1 đến 3 ---")
for i in range(1, 4): # Bảng cửu chương của số i
    print(f"--- Bảng cửu chương {i} ---")
    for j in range(1, 11): # Các phép nhân từ 1 đến 10
        print(f"{i} x {j} = {i * j}")
    print() # Xuống dòng sau mỗi bảng


# 8. List Comprehension với điều kiện (Nâng cao)
print("\n--- 8. Tạo danh sách các số chẵn từ 1 đến 20 ---")
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(f"Các số chẵn: {even_numbers}")


# 9. List Comprehension lồng nhau (Nâng cao) - Tạo ma trận
print("\n--- 9. Tạo ma trận 3x3 với giá trị (hàng, cột) ---")
matrix = [[(row, col) for col in range(3)] for row in range(3)]
for r in matrix:
    print(r)

"""
GHI CHÚ DỄ HIỂU CHO BẠN:

1.  Vòng lặp for dùng để làm gì?: 
    Tưởng tượng bạn có 1 rổ táo, "for" giúp bạn lấy TỪNG quả táo ra để kiểm tra cho đến khi hết rổ.

2.  Hàm range(số):
    - range(3): Tạo ra dãy 0, 1, 2 (bắt đầu từ 0 và dừng trước 3).
    - range(1, 6): Tạo ra dãy 1, 2, 3, 4, 5 (bắt đầu từ 1 và dừng trước 6).

3.  Biến chạy (như i,  char): 
    Là cái tên bạn tự đặt để đại diện cho phần tử đang được lấy ra trong lượt lặp đó.

4.  Mẹo nhỏ: Nếu bạn muốn lặp N lần mà không quan tâm đến giá trị của số đó, 
    hãy dùng `for _ in range(N):`. Dấu gạch dưới `_` báo hiệu cho người đọc là biến này không quan trọng.
    1. for + range()
2. for duyệt List/Tuple
3. for duyệt String
4. for lồng nhau
"""
