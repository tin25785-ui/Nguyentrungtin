"""Lời giải Bài tập Tuần 06: Vòng lặp while"""
import random

# TODO 1: Kiểm tra mật khẩu
password = ""
while password != "python123":
    password = input("Nhập mật khẩu: ")
    if password != "python123":
        print("Sai rồi! Thử lại.")
print("Truy cập thành công! ✅")

# TODO 2: Game đoán số
target = random.randint(1, 10)
guess = 0
print("--- Máy đã chọn 1 số từ 1-10 ---")

while guess != target:
    guess = int(input("Mời bạn đoán: "))
    if guess < target:
        print("Lớn hơn một chút!")
    elif guess > target:
        print("Nhỏ hơn một chút!")
print(f"Chúc mừng! Con số chính xác là {target} 🎉")