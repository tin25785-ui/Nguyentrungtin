"""
Bài tập 02: Xử lý dữ liệu CSV 📊
====================================
Mục tiêu: Đọc/ghi CSV với module csv
"""
import csv

# TODO 1: Tạo file "students.csv" với header và 5 dòng dữ liệu
# Header: Tên, Tuổi, Điểm Toán, Điểm Văn, Điểm Anh
# Dùng csv.writer
header = ["Tên", "Tuổi", "Điểm Toán", "Điểm Văn", "Điểm Anh"]
data = [
    ["Nguyễn An", 16, 9.0, 8.5, 9.5],
    ["Trần Bình", 17, 7.0, 8.0, 6.5],
    ["Lê Châu", 16, 5.5, 6.0, 5.0],
    ["Phạm Dũng", 18, 4.0, 3.5, 4.5],
    ["Hoàng Em", 17, 8.0, 7.5, 8.5]
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
print("--- Đã tạo file students.csv ---")

# TODO 2: Đọc file "students.csv" và in ra bảng đẹp
# Dùng csv.reader
print("\n--- Danh sách học sinh ---")
print(f"{'Tên':<15} {'Tuổi':<5} {'Toán':<7} {'Văn':<7} {'Anh':<7}")
print("-" * 45)
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Bỏ qua dòng tiêu đề
    for row in reader:
        print(f"{row[0]:<15} {row[1]:<5} {row[2]:<7} {row[3]:<7} {row[4]:<7}")

# TODO 3: Đọc CSV, tính điểm trung bình mỗi sinh viên
# In ra: "An: 8.0 điểm (Giỏi)"
def xep_loai(dtb):
    if dtb >= 8: return "Giỏi"
    if dtb >= 6.5: return "Khá"
    if dtb >= 5: return "Trung bình"
    return "Yếu"

print("\n--- Kết quả học tập ---")
with open("students.csv", "r", encoding="utf-8") as f:
    # Dùng DictReader để truy cập dữ liệu bằng tên cột cho dễ hiểu
    reader = csv.DictReader(f)
    for row in reader:
        dtb = (float(row["Điểm Toán"]) + float(row["Điểm Văn"]) + float(row["Điểm Anh"])) / 3
        loai = xep_loai(dtb)
        ten = row["Tên"].split()[-1] # Lấy tên cuối cho giống yêu cầu
        print(f"{ten}: {dtb:.1f} điểm ({loai})")

# TODO 4 (Thử thách): Đọc CSV, lọc sinh viên đạt (TB >= 5)
# Ghi danh sách đạt vào "passed.csv"
with open("students.csv", "r", encoding="utf-8") as f_in:
    reader = csv.DictReader(f_in)
    fieldnames = reader.fieldnames
    passed_students = []
    
    for row in reader:
        dtb = (float(row["Điểm Toán"]) + float(row["Điểm Văn"]) + float(row["Điểm Anh"])) / 3
        if dtb >= 5:
            passed_students.append(row)

with open("passed.csv", "w", newline="", encoding="utf-8") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(passed_students)
print(f"\n✅ Đã lọc {len(passed_students)} sinh viên đạt vào file passed.csv")
