"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
so_du = float(input("Nhập số dư hiện tại: "))
so_tien = float(input("Nhập số tiền muốn rút: "))

if so_tien > 0:
    if so_tien <= so_du:
        if so_tien % 50000 == 0:
            so_du -= so_tien
            print(f"Rút tiền thành công! Số dư còn lại: {so_du:,.0f} VNĐ")
        else:
            print("Lỗi: Số tiền rút phải là bội số của 50,000 VNĐ")
    else:
        print("Lỗi: Số dư không đủ để thực hiện giao dịch")
else:
    print("Lỗi: Số tiền rút phải lớn hơn 0")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
h = float(input("Nhập chiều cao (m): "))
w = float(input("Nhập cân nặng (kg): "))
bmi = w / (h ** 2)

print(f"Chỉ số BMI của bạn: {bmi:.1f}")
if bmi < 18.5:
    print("Thiếu cân — bạn nên bổ sung dinh dưỡng để tăng cân hợp lý.")
elif bmi < 25:
    print("Bình thường — chỉ số tuyệt vời, hãy duy trì nhé!")
elif bmi < 30:
    print("Thừa cân — bạn nên chú ý điều chỉnh chế độ ăn uống và tập luyện.")
else:
    print("Béo phì — bạn nên gặp bác sĩ để được tư vấn sức khỏe.")

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Loại vé (thuong/vip): ").lower()
ngay = input("Ngày (thuong/cuoi_tuan): ").lower()
tuoi = int(input("Nhập tuổi: "))

# 1. Xác định giá gốc theo loại vé
gia = 80000 if loai_ve == "thuong" else 120000

# 2. Phụ phí cuối tuần
if ngay == "cuoi_tuan":
    gia *= 1.3

# 3. Áp dụng giảm giá theo đối tượng (lồng nhau/phân cấp)
if tuoi < 12 or tuoi >= 65:
    gia *= 0.5
    print("- Giảm 50% cho trẻ em hoặc người cao tuổi")
elif 18 <= tuoi <= 25:
    gia *= 0.8
    print("- Giảm 20% cho sinh viên")

print(f"==> Giá vé cuối cùng của bạn là: {gia:,.0f} VNĐ")
