class NgayThangNam:
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
    def kiem_tra_hop_le(self):
        if self.thang < 1 or self.thang > 12:
            return False
        if self.ngay < 1 or self.ngay > 31:
            return False
        return True

    def ngay_hom_sau(self):
        self.ngay += 1
        if self.ngay > 30: 
            self.ngay = 1
            self.thang += 1
        if self.thang > 12:
            self.thang = 1
            self.nam += 1
        print(f"Ngày hôm sau là: {self.ngay}/{self.thang}/{self.nam}")
date = NgayThangNam(30, 12, 2023)
if date.kiem_tra_hop_le():
    date.ngay_hom_sau()