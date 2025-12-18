class NhanVien:
    def __init__(self, ma_nv, ten, luong_cb, he_so):
        self.ma_nv = ma_nv
        self.ten = ten
        self.luong_cb = luong_cb
        self.he_so = he_so

    def tinh_thuc_linh(self):
        return self.luong_cb * self.he_so

    def xuat_thong_tin(self):
        print(f"Nhân viên: {self.ten} - Thực lĩnh: {self.tinh_thuc_linh():,.0f} VNĐ")
nv = NhanVien("NV01", "Tran Thi B", 5000000, 2.5)
nv.xuat_thong_tin()