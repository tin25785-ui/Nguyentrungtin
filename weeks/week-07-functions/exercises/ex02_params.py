"""
Bài tập 02: Tham số nâng cao 🔧
=================================
Mục tiêu: Default args, *args, **kwargs
"""

# TODO 1: Hàm gioi_thieu(ten, tuoi=18, thanh_pho="Hà Nội")
# Gọi với: chỉ tên, tên + tuổi, tên + thành phố (keyword arg)
def gioi_thieu(ten, tuoi=18, thanh_pho="Hà Nội"):
    print(f"Tôi là {ten}, {tuoi} tuổi, ở {thanh_pho}")

gioi_thieu("An")
gioi_thieu("Bình", 25)
gioi_thieu("Châu", thanh_pho="Đà Nẵng")

# TODO 2: Hàm tinh_tong(*numbers) nhận số lượng tham số bất kỳ
# Trả về tổng
# tinh_tong(1, 2, 3) → 6
# tinh_tong(1, 2, 3, 4, 5) → 15
def tinh_tong(*numbers):
    return sum(numbers)

print(f"tinh_tong(1, 2, 3) = {tinh_tong(1, 2, 3)}")
print(f"tinh_tong(1, 2, 3, 4, 5) = {tinh_tong(1, 2, 3, 4, 5)}")

# TODO 3: Hàm tao_profile(**info)
# In ra thông tin dạng key: value
# tao_profile(ten="An", tuoi=25, nghe="Developer")
def tao_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

tao_profile(ten="An", tuoi=25, nghe="Developer")

# TODO 4: Lambda functions
# Tạo hàm lambda: binh_phuong, la_chan
# Dùng sorted() với key=lambda để sắp xếp list tuple theo phần tử thứ 2
students = [("An", 8.5), ("Bình", 7.0), ("Châu", 9.2)]

binh_phuong = lambda x: x**2
la_chan = lambda x: x % 2 == 0

print(f"Bình phương của 5: {binh_phuong(5)}")
print(f"8 là số chẵn? {la_chan(8)}")

sorted_students = sorted(students, key=lambda student: student[1])
print(f"Danh sách sắp xếp theo điểm: {sorted_students}")
