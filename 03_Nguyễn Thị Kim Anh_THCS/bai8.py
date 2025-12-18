class SanPham:
    def __init__(self, ten, don_gia, so_luong):
        self.ten = ten
        self._don_gia = don_gia 
        self._so_luong = so_luong
    @property
    def don_gia(self):
        return self._don_gia
    @don_gia.setter
    def don_gia(self, gia_moi):
        if gia_moi < 0:
            print("Lỗi: Giá không được âm!")
        else:
            self._don_gia = gia_moi

    def tinh_tien(self):
        return self._don_gia * self._so_luong
sp = SanPham("Laptop", 1000, 2)
sp.don_gia = -500 
print(f"Giá hiện tại: {sp.don_gia}") 
sp.don_gia = 1200 
print(f"Giá mới: {sp.don_gia}")