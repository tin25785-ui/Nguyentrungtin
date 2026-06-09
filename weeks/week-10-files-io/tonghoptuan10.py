"""
TỔNG HỢP KIẾN THỨC TUẦN 10: FILE I/O 📂
=======================================
Mục tiêu: Nắm vững cách đọc, ghi, và quản lý file trong Python.
So sánh với C++ để hiểu sâu hơn về bản chất.
"""

import csv
import json
from pathlib import Path

# ==========================================
# 1. ĐỌC VÀ GHI FILE TEXT VỚI open()
# ==========================================
# C++: Tương đương với std::ofstream (ghi), std::ifstream (đọc), std::fstream (cả hai).
# Python: Hàm open() trả về một đối tượng file, sau đó dùng các phương thức của nó.

print("--- 1. Đọc và Ghi File Text ---")

# Chế độ 'w' (write): Ghi đè file nếu đã tồn tại, tạo mới nếu chưa.
# Luôn dùng encoding='utf-8' cho tiếng Việt.
with open("my_file.txt", "w", encoding="utf-8") as f:
    f.write("Đây là dòng đầu tiên.\n")
    f.write("Đây là dòng thứ hai.\n")
    print("✅ Đã ghi nội dung vào my_file.txt (chế độ 'w').")

# Chế độ 'a' (append): Thêm nội dung vào cuối file.
with open("my_file.txt", "a", encoding="utf-8") as f:
    f.write("Dòng này được thêm vào cuối.\n")
    print("✅ Đã thêm nội dung vào my_file.txt (chế độ 'a').")

# Chế độ 'r' (read): Đọc nội dung từ file.
with open("my_file.txt", "r", encoding="utf-8") as f:
    content = f.read() # Đọc toàn bộ nội dung
    print("\nNội dung từ my_file.txt (f.read()):")
    print(content)

with open("my_file.txt", "r", encoding="utf-8") as f:
    print("\nNội dung từ my_file.txt (đọc từng dòng):")
    for line in f:
        print(f"- {line.strip()}") # .strip() để bỏ ký tự xuống dòng '\n'


# ==========================================
# 2. CONTEXT MANAGER (with)
# ==========================================
# C++: Tương đương với RAII (Resource Acquisition Is Initialization),
#      ví dụ: đối tượng std::fstream tự động đóng file khi ra khỏi scope.
# Python: 'with' đảm bảo file luôn được đóng tự động, ngay cả khi có lỗi.

print("\n--- 2. Context Manager (with) ---")
try:
    with open("non_existent_file.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("❌ Lỗi: File không tồn tại, nhưng 'with' vẫn đảm bảo không có rò rỉ tài nguyên.")


# ==========================================
# 3. XỬ LÝ DỮ LIỆU CSV VỚI MODULE csv
# ==========================================
# C++: Thường phải tự phân tích chuỗi hoặc dùng thư viện bên thứ ba.
# Python: Module 'csv' cung cấp các công cụ mạnh mẽ để đọc/ghi dữ liệu dạng bảng.

print("\n--- 3. Xử lý Dữ liệu CSV ---")

# Dữ liệu mẫu
students_data = [
    ["Tên", "Tuổi", "Điểm"],
    ["An", 18, 8.5],
    ["Bình", 19, 7.0],
    ["Châu", 18, 9.2]
]

# Ghi file CSV
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students_data)
    print("✅ Đã ghi dữ liệu vào students.csv.")

# Đọc file CSV
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("\nNội dung từ students.csv:")
    for row in reader:
        print(row)

# Đọc CSV dưới dạng Dictionary (DictReader)
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("\nNội dung từ students.csv (DictReader):")
    for row in reader:
        print(f"Tên: {row['Tên']}, Điểm: {row['Điểm']}")


# ==========================================
# 4. ĐỌC/GHI JSON VỚI MODULE json
# ==========================================
# C++: Thường dùng thư viện bên thứ ba như nlohmann/json.
# Python: Module 'json' tích hợp sẵn, dễ dàng chuyển đổi giữa dict/list Python và chuỗi JSON.

print("\n--- 4. Đọc/Ghi JSON ---")

# Dữ liệu Python (dict)
config_data = {
    "app_name": "MyPythonApp",
    "version": "1.0.0",
    "settings": {
        "debug_mode": True,
        "language": "vi"
    },
    "users": ["admin", "guest"]
}

# Ghi dict vào file JSON
# indent=4: định dạng đẹp, dễ đọc
# ensure_ascii=False: giữ nguyên ký tự tiếng Việt
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config_data, f, indent=4, ensure_ascii=False)
    print("✅ Đã ghi dữ liệu vào config.json.")

# Đọc file JSON vào dict Python
with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)
    print("\nNội dung từ config.json:")
    print(f"Tên ứng dụng: {loaded_config['app_name']}")
    print(f"Chế độ debug: {loaded_config['settings']['debug_mode']}")


# ==========================================
# 5. DÙNG pathlib ĐỂ THAO TÁC ĐƯỜNG DẪN
# ==========================================
# C++: Tương đương với std::filesystem (từ C++17).
# Python: Module 'pathlib' cung cấp cách tiếp cận hướng đối tượng, trực quan hơn.

print("\n--- 5. Thao tác Đường dẫn với pathlib ---")

# Tạo đối tượng Path
current_dir = Path.cwd()
print(f"Thư mục hiện tại: {current_dir}")

# Tạo đường dẫn mới
file_path = current_dir / "data" / "my_report.txt" # Nối đường dẫn một cách an toàn
print(f"Đường dẫn file báo cáo: {file_path}")

# Kiểm tra sự tồn tại
print(f"File 'my_file.txt' có tồn tại không? {Path('my_file.txt').exists()}")
print(f"Thư mục 'data' có tồn tại không? {Path('data').is_dir()}")

# Tạo thư mục (nếu chưa có)
data_dir = Path("data")
data_dir.mkdir(exist_ok=True) # exist_ok=True tránh lỗi nếu thư mục đã có
print(f"✅ Đã đảm bảo thư mục 'data' tồn tại.")

# Ghi file qua pathlib
new_file = data_dir / "log.txt"
new_file.write_text("Đây là log đầu tiên.\n", encoding="utf-8")
print(f"✅ Đã ghi file '{new_file}' qua pathlib.")

# Đọc file qua pathlib
print(f"\nNội dung từ '{new_file}':")
print(new_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    print("\n--- Hoàn thành tổng hợp Tuần 10 ---")
    # Dọn dẹp các file đã tạo để chạy lại ví dụ
    # Path("my_file.txt").unlink(missing_ok=True)
    # Path("students.csv").unlink(missing_ok=True)
    # Path("config.json").unlink(missing_ok=True)
    # Path("data/log.txt").unlink(missing_ok=True)
    # Path("data").rmdir() # Chỉ xóa thư mục rỗng
    # print("\nĐã dọn dẹp các file/thư mục tạm thời.")