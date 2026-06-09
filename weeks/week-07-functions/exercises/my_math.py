"""
Module my_math cung cấp các hàm toán học cơ bản.
"""

def cong(a, b):
    """Trả về tổng của a và b."""
    return a + b

def tru(a, b):
    """Trả về hiệu của a và b."""
    return a - b

def nhan(a, b):
    """Trả về tích của a và b."""
    return a * b

def chia(a, b):
    """Trả về thương của a và b. Có xử lý lỗi chia cho 0."""
    return a / b if b != 0 else "Lỗi: Không thể chia cho 0"

def luy_thua(a, b):
    """Trả về giá trị a lũy thừa b."""
    return a ** b