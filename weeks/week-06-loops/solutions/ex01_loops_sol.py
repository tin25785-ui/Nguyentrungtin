"""Lời giải Bài tập Tuần 06: Vòng lặp for"""

# TODO 1: Số lẻ từ 1-20
print("Số lẻ từ 1-20:")
for i in range(1, 21, 2):
    print(i, end=" ")
print("\n")

# TODO 2: Tổng từ 1 đến n
n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1):
    tong += i
print(f"Tổng từ 1 đến {n} là: {tong}")

# TODO 3: Tìm số lớn nhất không dùng max()
nums = [12, 45, 7, 23, 56, 10]
max_val = nums[0]
for n in nums:
    if n > max_val:
        max_val = n
print(f"Số lớn nhất là: {max_val}")

# TODO 4: Bảng cửu chương
num = int(input("Bảng cửu chương số mấy? "))
print(f"--- Bảng cửu chương {num} ---")
for i in range(1, 11):
    print(f"{num} x {i:>2} = {num * i:>2}")