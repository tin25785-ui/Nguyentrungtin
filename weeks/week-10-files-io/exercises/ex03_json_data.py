"""
Bài tập 03: Đọc/ghi JSON 📋
==============================
Mục tiêu: Dùng module json để lưu trữ dữ liệu có cấu trúc
"""
import json
from datetime import datetime

# TODO 1: Tạo dict config và ghi vào "config.json"
# config = {"app_name": "MyApp", "version": "1.0", "debug": True}
config = {"app_name": "MyApp", "version": "1.0", "debug": True}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)
print("--- Đã tạo file config.json ---")

# TODO 2: Đọc "config.json" và in ra từng key-value
print("\n--- Nội dung cấu hình ---")
with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    for key, value in data.items():
        print(f"{key}: {value}")

# TODO 3: Tạo list of dicts (sản phẩm) và ghi vào "products.json"
# Mỗi sản phẩm có: ten, gia, so_luong
# Dùng json.dump() với indent=2, ensure_ascii=False
products = [
    {"ten": "Điện thoại iPhone 15", "gia": 22000000, "so_luong": 10},
    {"ten": "Máy tính bảng iPad", "gia": 12000000, "so_luong": 15},
    {"ten": "Tai nghe AirPods", "gia": 4500000, "so_luong": 30}
]

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)
print("\n--- Đã tạo file products.json thành công ---")

# TODO 4 (Thử thách): Sổ ghi chú JSON
# Viết chương trình: thêm ghi chú → lưu JSON → đọc lại → hiển thị
# Mỗi ghi chú có: noi_dung, ngay_tao (dùng datetime)
def so_ghi_chu():
    file_notes = "notes.json"
    
    # Bước 1: Đọc dữ liệu cũ (nếu có)
    try:
        with open(file_notes, "r", encoding="utf-8") as f:
            all_notes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        all_notes = []

    # Bước 2: Thêm ghi chú mới
    print("\n--- THÊM GHI CHÚ MỚI ---")
    content = input("Nhập nội dung ghi chú: ")
    if content:
        new_note = {
            "noi_dung": content,
            "ngay_tao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        all_notes.append(new_note)

        # Bước 3: Lưu lại vào file
        with open(file_notes, "w", encoding="utf-8") as f:
            json.dump(all_notes, f, indent=2, ensure_ascii=False)
        print("✅ Đã lưu ghi chú!")

    # Bước 4: Hiển thị lại toàn bộ
    if all_notes:
        print("\n--- TẤT CẢ GHI CHÚ TRONG FILE ---")
        for i, note in enumerate(all_notes, 1):
            print(f"{i}. [{note['ngay_tao']}] {note['noi_dung']}")
    else:
        print("Sổ ghi chú đang trống.")

# Chạy thử chương trình sổ ghi chú
if __name__ == "__main__":
    so_ghi_chu()
