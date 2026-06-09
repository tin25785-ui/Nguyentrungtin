"""
So sánh List và Tuple trong Python 
====================================
1. List: Dùng ngoặc vuông [], có thể thay đổi (Mutable).
2. Tuple: Dùng ngoặc tròn (), không thể thay đổi (Immutable).
"""

# Ví dụ 1: Khả năng thay đổi (Mutability)
print("--- Ví dụ 1: Khả năng thay đổi ---")

# List cho phép sửa đổi nội dung
fruit_list = ["Táo", "Chuối", "Cam"]
fruit_list[1] = "Dâu tây"  # Thay đổi Chuối thành Dâu tây
fruit_list.append("Xoài")  # Thêm phần tử mới
print(f"List (Sau khi sửa): {fruit_list}")

# Tuple KHÔNG cho phép sửa đổi
coordinates = (10, 20)
print(f"Tuple (Tọa độ gốc): {coordinates}")
# coordinates[0] = 15  # Dòng này sẽ gây LỖI (TypeError) nếu bạn bỏ comment
print("Lưu ý: Tuple không thể dùng append() hay thay đổi giá trị trực tiếp.")


# Ví dụ 2: Ý nghĩa sử dụng thực tế
print("\n--- Ví dụ 2: Ý nghĩa sử dụng ---")

# List: Thường dùng cho danh sách các đối tượng cùng loại có thể biến động (VD: danh sách việc cần làm)
todo_list = ["Học Python", "Đi chợ", "Nấu cơm"]
print(f"Danh sách việc cần làm (List): {todo_list}")

# Tuple: Thường dùng cho các bản ghi dữ liệu có cấu trúc cố định (VD: Thông tin sinh viên)
student_info = ("Nguyễn Trung Tín", 19, "TP.HCM")
print(f"Thông tin sinh viên (Tuple): Tên={student_info[0]}, Tuổi={student_info[1]}")

print("\n=> Tóm lại: Dùng List khi cần thêm/xóa/sửa. Dùng Tuple khi muốn bảo vệ dữ liệu không bị thay đổi.")