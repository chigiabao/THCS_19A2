from abc import ABC, abstractmethod
import math

class HinhHoc(ABC):
    @abstractmethod
    def tinh_dien_tich(self):
        pass

class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.r = ban_kinh
    
    def tinh_dien_tich(self):
        return math.pi * self.r * self.r

class HinhVuong(HinhHoc):
    def __init__(self, canh):
        self.canh = canh
    
    def tinh_dien_tich(self):
        return self.canh * self.canh
danh_sach_hinh = [HinhTron(5), HinhVuong(4), HinhTron(2)]
for h in danh_sach_hinh:
    print(f"Diện tích: {h.tinh_dien_tich():.2f}")