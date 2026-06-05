"""
Bài tập 01: Tạo và thao tác List 📋
=====================================
Mục tiêu: Thành thạo CRUD trên list
"""

# TODO 1: Tạo list 5 môn học yêu thích
# Thêm 1 môn bằng append(), chèn 1 môn vào vị trí 2 bằng insert()
# Xóa 1 môn bằng remove(), in list sau mỗi thao tác
subjects = ["Toán", "Lý", "Hóa", "Văn", "Anh"]
print(f"Danh sách ban đầu: {subjects}")

subjects.append("Sinh")
print(f"Sau khi append: {subjects}")

subjects.insert(2, "Địa")
print(f"Sau khi insert vào vị trí 2: {subjects}")

subjects.remove("Hóa")
print(f"Sau khi xóa 'Hóa': {subjects}")


# TODO 2: Cho diem = [7, 9, 5, 8, 10, 6, 4, 9]
# a) Sắp xếp tăng dần (tại chỗ)
# b) Tìm điểm cao nhất, thấp nhất, trung bình
# c) Đếm số điểm >= 5 (đạt)
diem = [7, 9, 5, 8, 10, 6, 4, 9]
diem.sort()
print(f"Sắp xếp tăng dần: {diem}")
print(f"Cao nhất: {max(diem)}, Thấp nhất: {min(diem)}, Trung bình: {sum(diem)/len(diem)}")
dat = len([s for s in diem if s >= 5])
print(f"Số lượng điểm đạt (>=5): {dat}")

# TODO 3: Nhập n số từ người dùng, lưu vào list
# In ra: tổng, trung bình, min, max
n = int(input("Nhập số lượng phần tử n: "))
user_list = []
for i in range(n):
    val = float(input(f"Nhập số thứ {i+1}: "))
    user_list.append(val)

print(f"Tổng: {sum(user_list)}")
print(f"Trung bình: {sum(user_list)/len(user_list)}")
print(f"Min: {min(user_list)}, Max: {max(user_list)}")

# TODO 4 (Thử thách): Xóa phần tử trùng lặp khỏi list
# Cho nums = [1, 3, 2, 3, 1, 5, 2, 4]
# Kết quả: [1, 3, 2, 5, 4] (giữ thứ tự xuất hiện đầu tiên)
# KHÔNG dùng set()
nums = [1, 3, 2, 3, 1, 5, 2, 4]
unique_nums = []
for x in nums:
    if x not in unique_nums:
        unique_nums.append(x)
print(f"List sau khi lọc trùng: {unique_nums}")
