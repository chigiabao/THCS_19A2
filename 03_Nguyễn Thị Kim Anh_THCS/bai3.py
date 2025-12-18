import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rut_gon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        return self

    def cong(self, ps_khac):
        tu_moi = self.tu * ps_khac.mau + ps_khac.tu * self.mau
        mau_moi = self.mau * ps_khac.mau
        return PhanSo(tu_moi, mau_moi).rut_gon()

    def hien_thi(self):
        print(f"{self.tu}/{self.mau}")
ps1 = PhanSo(1, 2)
ps2 = PhanSo(3, 4)
tong = ps1.cong(ps2)
print("Tổng 2 phân số: ", end="")
tong.hien_thi() 