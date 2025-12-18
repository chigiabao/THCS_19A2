from abc import ABC, abstractmethod
class ITienDien(ABC):
    @abstractmethod
    def tinh_tien(self, so_kw):
        pass

class HoGiaDinh(ITienDien):
    def tinh_tien(self, so_kw):
        if so_kw <= 50:
            return so_kw * 1500
        else:
            return 50 * 1500 + (so_kw - 50) * 2000

class DoanhNghiep(ITienDien):
    def tinh_tien(self, so_kw):
        return so_kw * 3000
khach_hang_a = HoGiaDinh()
khach_hang_b = DoanhNghiep()

print(f"Hộ dân (100kW): {khach_hang_a.tinh_tien(100)}")
print(f"Doanh nghiệp (100kW): {khach_hang_b.tinh_tien(100)}")