class SanPham:
    def __init__(self, ten, don_gia, so_luong):
        self.ten = ten
        self.don_gia = don_gia
        self.so_luong = so_luong

    def tinh_tien(self):
        return self.don_gia * self.so_luong
class DonHang:
    def __init__(self):
        self.danh_sach_sp = [] 

    def them_san_pham(self, sp):
        self.danh_sach_sp.append(sp)

    def tinh_tong_tien(self):
        tong = 0
        for sp in self.danh_sach_sp:
            tong += sp.tinh_tien() 
        
        thue_vat = tong * 0.08
        return tong + thue_vat
dh = DonHang()
dh.them_san_pham(SanPham("Chuột", 100, 2))    
dh.them_san_pham(SanPham("Bàn phím", 200, 1)) 
print(f"Tổng tiền thanh toán (gồm VAT): {dh.tinh_tong_tien()}")