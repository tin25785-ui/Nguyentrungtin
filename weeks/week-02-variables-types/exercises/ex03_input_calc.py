"""
Bài tập 03: Máy tính đơn giản nhận input 🧮
"""

print("--- CHƯƠNG TRÌNH TÍNH TỔNG ---")

# input() luôn trả về chuỗi, nên cần ép kiểu ngay
so_a = float(input("Nhập số thứ nhất: "))
so_b = float(input("Nhập số thứ hai: "))

ket_qua = so_a + so_b

print(f"Tổng của {so_a} và {so_b} là: {ket_qua}")