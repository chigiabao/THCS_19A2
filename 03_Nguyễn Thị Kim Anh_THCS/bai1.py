class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_tb):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tb = diem_tb

    def xep_loai(self):
        if self.diem_tb >= 8.0:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5.0:
            return "Trung Bình"
        else:
            return "Yếu"

    def hien_thi(self):
        print(f"SV: {self.ho_ten} ({self.ma_sv}) - Điểm: {self.diem_tb} - Xếp loại: {self.xep_loai()}")
sv1 = SinhVien("SV001", "Nguyen Van A", 8.5)
sv1.hien_thi()