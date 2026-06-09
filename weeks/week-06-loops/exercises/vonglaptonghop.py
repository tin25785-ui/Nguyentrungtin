"""
TỔNG HỢP KIẾN THỨC VÒNG LẶP (FOR & WHILE) 🔄
==========================================
File này tổng hợp các cách dùng vòng lặp phổ biến trong Python.
"""

# 1. Vòng lặp FOR với range() - Dùng khi biết trước số lần lặp
print("--- 1. Duyệt số từ 1 đến 5 ---")
for i in range(1, 6):
    print(f"Lần lặp thứ: {i}")


# 2. Duyệt List với enumerate() - Lấy cả vị trí (index) và giá trị
print("\n--- 2. Duyệt danh sách kèm số thứ tự ---")
ds_mon_hoc = ["Toán", "Lý", "Hóa", "Sinh"]
for index, mon in enumerate(ds_mon_hoc, start=1):
    print(f"Môn {index}: {mon}")


# 3. Vòng lặp WHILE - Dùng khi lặp theo điều kiện (chưa biết trước số lần)
print("\n--- 3. Kiểm tra dữ liệu nhập vào (While True) ---")
while True:
    diem = input("Nhập điểm (0-10) để thoát: ")
    if diem.replace('.', '', 1).isdigit(): # Kiểm tra xem có phải là số không
        diem = float(diem)
        if 0 <= diem <= 10:
            print(f"Bạn đã nhập điểm hợp lệ: {diem}")
            break # Thoát vòng lặp khi điều kiện thỏa mãn
    print("Lỗi: Vui lòng nhập số trong khoảng 0-10!")


# 4. Điều khiển vòng lặp: BREAK và CONTINUE
print("\n--- 4. Ví dụ về Break và Continue ---")
print("In các số từ 1-10, bỏ qua số 3 và dừng khi gặp số 7:")
for n in range(1, 11):
    if n == 3:
        continue  # Nhảy qua các lệnh bên dưới, bắt đầu lần lặp tiếp theo
    if n == 7:
        break     # Thoát hẳn vòng lặp
    print(n, end=" ")
print()


# 5. Vòng lặp lồng nhau (Nested Loops) - Thường dùng cho dữ liệu 2 chiều
print("\n--- 5. Vẽ hình chữ nhật bằng dấu sao ---")
rows = 3
cols = 5
for r in range(rows):
    for c in range(cols):
        print("*", end=" ")
    print() # Xuống dòng sau mỗi hàng


# 6. Ghép cặp danh sách với zip()
print("\n--- 6. Ghép cặp Tên và Điểm ---")
names = ["An", "Bình", "Chi"]
scores = [8.5, 9.0, 7.5]
for name, score in zip(names, scores):
    print(f"Học sinh {name} đạt {score} điểm")


# 7. List Comprehension - Cách viết vòng lặp siêu ngắn gọn (Nâng cao)
print("\n--- 7. Tạo danh sách bình phương từ 1-5 ---")
squares = [x**2 for x in range(1, 6)]
print(f"Kết quả: {squares}")

"""
GHI CHÚ QUAN TRỌNG:
1. Chọn FOR: Khi bạn biết rõ cần duyệt qua bao nhiêu phần tử hoặc một dãy số.
2. Chọn WHILE: Khi bạn đợi một điều kiện nào đó thành SAI (như nhập sai pass, chờ sensor...).
3. Cẩn thận vòng lặp vô tận: Luôn đảm bảo điều kiện của While sẽ có lúc thành False hoặc có lệnh Break.
4. enumerate() và zip() là hai "vũ khí" cực mạnh giúp code Python sạch đẹp hơn.
"""