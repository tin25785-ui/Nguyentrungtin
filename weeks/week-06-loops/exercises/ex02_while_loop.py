"""
Bài tập 02: Vòng lặp while ⏳
================================
Mục tiêu: Dùng while với điều kiện kiểm soát
"""

# TODO 1: Đếm ngược từ 10 → 1, in "Phóng! 🚀"
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Phóng! 🚀")

# TODO 2: Trò chơi đoán số
# Máy chọn số bí mật (random.randint(1, 100))
# Người dùng đoán, máy gợi ý "Cao hơn!" hoặc "Thấp hơn!"
# Đếm số lần đoán
import random
secret = random.randint(1, 100)
attempts = 0
print("Máy đã chọn một số bí mật từ 1-100.")
while True:
    guess = int(input("Mời bạn đoán: "))
    attempts += 1
    if guess < secret:
        print("Cao hơn!")
    elif guess > secret:
        print("Thấp hơn!")
    else:
        print(f"Chúc mừng! Bạn đã đoán đúng sau {attempts} lần.")
        break

# TODO 3: Nhập liệu an toàn
# Hỏi nhập tuổi, lặp lại cho đến khi người dùng nhập số hợp lệ (1-120)
# Dùng while True + break
while True:
    tuoi_str = input("Nhập tuổi của bạn (1-120): ")
    if tuoi_str.isdigit():
        tuoi = int(tuoi_str)
        if 1 <= tuoi <= 120:
            break
    print("Tuổi không hợp lệ, vui lòng nhập lại.")
print(f"Tuổi của bạn là: {tuoi}")

# TODO 4 (Thử thách): Menu chương trình
# Hiển thị menu: 1. Cộng, 2. Trừ, 3. Nhân, 4. Thoát
# Lặp lại đến khi người dùng chọn 4
while True:
    print("\n--- MENU ---")
    print("1. Cộng\n2. Trừ\n3. Nhân\n4. Thoát")
    choice = input("Chọn chức năng: ")
    if choice == '4':
        print("Tạm biệt!")
        break
    if choice in ('1', '2', '3'):
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        if choice == '1': print(f"Kết quả: {a + b}")
        elif choice == '2': print(f"Kết quả: {a - b}")
        elif choice == '3': print(f"Kết quả: {a * b}")
    else:
        print("Lựa chọn không hợp lệ.")
