"""
Bài tập 03: Tuple & Unpacking 📦
==================================
Mục tiêu: Hiểu tuple và khi nào dùng
"""

# TODO 1: Tạo tuple lưu tọa độ (x, y) = (3, 7)
# In ra x và y bằng unpacking
# Thử gán lại giá trị cho tuple — quan sát lỗi gì xảy ra?
point = (3, 7)
x, y = point
print(f"Tọa độ: x={x}, y={y}")
# point[0] = 10  # Lỗi TypeError: 'tuple' object does not support item assignment

# TODO 2: Hàm trả về tuple
# Viết hàm tinh_thong_ke(numbers) nhận list số
# Trả về tuple: (min, max, trung_binh)
# Gọi hàm và unpack kết quả
def tinh_thong_ke(numbers):
    return (min(numbers), max(numbers), sum(numbers)/len(numbers))

res_min, res_max, res_avg = tinh_thong_ke([10, 20, 30, 40, 50])
print(f"Thống kê: Min={res_min}, Max={res_max}, TB={res_avg}")

# TODO 3: Cho danh sách sinh viên dạng list of tuples:
# students = [("An", 8.5), ("Bình", 7.0), ("Châu", 9.2), ("Dũng", 6.5)]
# a) In ra tên và điểm mỗi sinh viên (dùng unpacking trong for)
# b) Tìm sinh viên có điểm cao nhất
# c) Sắp xếp theo điểm giảm dần
students = [("An", 8.5), ("Bình", 7.0), ("Châu", 9.2), ("Dũng", 6.5)]
# a
for name, score in students:
    print(f"Sinh viên {name} - Điểm: {score}")
# b
best_student = max(students, key=lambda x: x[1])
print(f"Sinh viên ưu tú nhất: {best_student[0]} ({best_student[1]})")
# c
students.sort(key=lambda x: x[1], reverse=True)
print(f"Danh sách sau khi sắp xếp điểm giảm dần: {students}")

# TODO 4 (Thử thách): Swap & enumerate
# Cho 2 list: names = ["A", "B", "C"], scores = [8, 9, 7]
# Dùng enumerate + zip để in:
# 1. A — 8 điểm
# 2. B — 9 điểm
# 3. C — 7 điểm
names = ["A", "B", "C"]
scores_val = [8, 9, 7]
for i, (n, s) in enumerate(zip(names, scores_val), start=1):
    print(f"{i}. {n} — {s} điểm")
