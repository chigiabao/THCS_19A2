class Nguoi:
    def __init__(self, ten, nam_sinh):
        self.ten = ten
        self.nam_sinh = nam_sinh

    def hien_thi(self):
        print(f"Họ tên: {self.ten} - Năm sinh: {self.nam_sinh}")

class HocSinh(Nguoi):
    def __init__(self, ten, nam_sinh, lop, diem_tb):
        super().__init__(ten, nam_sinh) 
        self.lop = lop
        self.diem_tb = diem_tb
    def hien_thi(self):
        super().hien_thi()
        print(f"Lớp: {self.lop} - Điểm TB: {self.diem_tb}")
hs = HocSinh("Le Van C", 2005, "12A1", 9.0)
hs.hien_thi()