"""Lời giải Bài tập 03: Tuple và Unpacking"""

# TODO 1: Tạo một tuple chứa tọa độ x, y
point = (10, 20)
print(f"Tọa độ ban đầu: {point}")

# TODO 2: Giải nén (Unpacking) tuple vào hai biến x và y
x, y = point
print(f"Biến x: {x}, Biến y: {y}")

# TODO 3: Tuple lồng nhau - Lưu thông tin sinh viên (Tên, (Toán, Lý, Hóa))
student = ("Bình", (8, 9, 7))
name, scores = student
print(f"Sinh viên {name} có điểm trung bình là: {sum(scores)/len(scores):.2f}")

# TODO 4: Chuyển đổi một List thành Tuple để bảo vệ dữ liệu (không cho sửa)
colors_list = ["đỏ", "xanh", "vàng"]
colors_tuple = tuple(colors_list)
print(f"List đã chuyển thành Tuple: {colors_tuple}")
# colors_tuple[0] = "tím"  # Dòng này sẽ gây lỗi vì Tuple là immutable