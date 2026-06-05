"""Lời giải Bài tập 02: Các phương thức xử lý List số học"""

numbers = [45, 12, 89, 7, 34, 12, 56]
print(f"Danh sách số: {numbers}")

# TODO 1: Đếm số lần xuất hiện của số 12
count_12 = numbers.count(12)
print(f"Số 12 xuất hiện {count_12} lần")

# TODO 2: Tìm giá trị lớn nhất (max), nhỏ nhất (min) và tổng (sum)
print(f"Giá trị lớn nhất: {max(numbers)}")
print(f"Giá trị nhỏ nhất: {min(numbers)}")
print(f"Tổng các số: {sum(numbers)}")

# TODO 3: Sắp xếp danh sách tăng dần và giảm dần
numbers.sort()
print(f"Sắp xếp tăng dần: {numbers}")

numbers.sort(reverse=True)
print(f"Sắp xếp giảm dần: {numbers}")