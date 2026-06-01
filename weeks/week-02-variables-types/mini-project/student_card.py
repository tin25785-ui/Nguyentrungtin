"""
Mini-Project Tuần 02: Thẻ sinh viên tự động 🪪
"""

# 1. Nhập dữ liệu
ho_ten = input("Nhập họ tên: ")
mssv = input("Nhập MSSV: ")
nganh_hoc = input("Nhập ngành học: ")
nam_nhap_hoc = int(input("Nhập năm nhập học: "))

# 2. Xử lý dữ liệu
ho_ten_dep = ho_ten.upper()          # Viết hoa toàn bộ tên
nganh_dep = nganh_hoc.title()        # Viết hoa chữ cái đầu mỗi từ
nam_tot_nghiep = nam_nhap_hoc + 4    # Tính năm tốt nghiệp

# 3. Hiển thị thẻ sinh viên
print("\n" + "═" * 30)
print(f"║ {'THẺ SINH VIÊN':^26} ║")
print("║" + "-" * 28 + "║")
print(f"║ Họ tên: {ho_ten_dep:<19} ║")
print(f"║ MSSV:   {mssv:<19} ║")
print(f"║ Ngành:  {nganh_dep:<19} ║")
print(f"║ Khóa:   {nam_nhap_hoc} - {nam_tot_nghiep:<10} ║")
print("╚" + "═" * 28 + "╝")