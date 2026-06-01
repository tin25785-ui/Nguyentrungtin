"""
Mini-Project Tuần 04: Text Analyzer 📝
=====================================
Phân tích văn bản: đếm từ, câu, tần suất và tìm từ đặc biệt.
"""

print("--- CHƯƠNG TRÌNH PHÂN TÍCH VĂN BẢN ---")
print("(Nhập đoạn văn bản của bạn và nhấn Enter để phân tích)\n")

# 1. Nhập đoạn văn bản
text = input("Nội dung: ").strip()

if not text:
    print("Văn bản trống, không có gì để phân tích!")
else:
    # 2. Tiền xử lý dữ liệu
    # Đếm số câu (dựa trên các dấu kết thúc)
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    if num_sentences == 0 and len(text) > 0: num_sentences = 1 # Trường hợp không có dấu chấm cuối câu

    # Tách từ và loại bỏ dấu câu cơ bản để đếm chính xác
    raw_words = text.lower().split()
    words = [w.strip(".,!?;:\"()[]{}") for w in raw_words if w.strip(".,!?;:\"()[]{}")]
    
    # 3. Tính toán các chỉ số
    num_chars = len(text)
    num_words = len(words)
    
    # Tìm từ dài nhất và ngắn nhất
    longest_word = max(words, key=len) if words else ""
    shortest_word = min(words, key=len) if words else ""

    # 4. Đếm tần suất xuất hiện (Dùng Dictionary)
    word_freq = {}
    for w in words:
        word_freq[w] = word_freq.get(w, 0) + 1

    # Sắp xếp để lấy Top 5 từ xuất hiện nhiều nhất
    # (Chuyển dict thành list các tuple rồi sắp xếp theo số lượng giảm dần)
    sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    top_5 = sorted_freq[:5]

    # 5. In thống kê tổng hợp với f-string
    print("\n" + "="*40)
    print(f"{'THỐNG KÊ CHI TIẾT':^40}")
    print("-" * 40)
    print(f"🔹 Số ký tự:      {num_chars:>10}")
    print(f"🔹 Số từ:         {num_words:>10}")
    print(f"🔹 Số câu:        {num_sentences:>10}")
    print(f"🔹 Từ dài nhất:   '{longest_word}' ({len(longest_word)} ký tự)")
    print(f"🔹 Từ ngắn nhất:  '{shortest_word}' ({len(shortest_word)} ký tự)")
    
    print("\n📊 Top 5 từ xuất hiện nhiều nhất:")
    for word, count in top_5:
        # Tạo hiệu ứng biểu đồ thanh đơn giản
        bar = "█" * count
        print(f"  - {word:<12} {bar} ({count} lần)")
    
    print("="*40)

print("\nCảm ơn bạn đã sử dụng Text Analyzer!")