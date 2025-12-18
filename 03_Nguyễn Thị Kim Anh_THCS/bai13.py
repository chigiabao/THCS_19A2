class NhanVien:
    def __init__(self, ten):
        self.ten = ten
    
    def tinh_luong(self):
        return 0

class NhanVienSanXuat(NhanVien):
    def __init__(self, ten, so_san_pham):
        super().__init__(ten)
        self.so_san_pham = so_san_pham
    
    def tinh_luong(self):
        return self.so_san_pham * 5000

class NhanVienVanPhong(NhanVien):
    def __init__(self, ten, ngay_cong):
        super().__init__(ten)
        self.ngay_cong = ngay_cong
    
    def tinh_luong(self):
        return self.ngay_cong * 200000
nv1 = NhanVienSanXuat("Anh Nam", 100)
nv2 = NhanVienVanPhong("Chi Lan", 22)

print(f"Lương {nv1.ten}: {nv1.tinh_luong()}")
print(f"Lương {nv2.ten}: {nv2.tinh_luong()}")