class TaiKhoan:
    def __init__(self, so_du=0):
        self.so_du = so_du

    def rut_tien(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
            print(f"Đã rút {so_tien}. Còn lại: {self.so_du}")
        else:
            print("Không đủ tiền!")

class TaiKhoanTietKiem(TaiKhoan):
    def rut_tien(self, so_tien):
        if self.so_du - so_tien >= 50000:
            self.so_du -= so_tien
            print(f"[TK Tiết Kiệm] Rút thành công {so_tien}. Còn lại: {self.so_du}")
        else:
            print("[TK Tiết Kiệm] Thất bại! Phải duy trì số dư tối thiểu 50k.")

class TaiKhoanThanhToan(TaiKhoan):
    def rut_tien(self, so_tien):
        tong_tru = so_tien + 5000
        if self.so_du >= tong_tru:
            self.so_du -= tong_tru
            print(f"[TK Thanh Toán] Rút {so_tien} (Phí 5k). Còn lại: {self.so_du}")
        else:
            print("Không đủ tiền trả cả phí!")
tk1 = TaiKhoanTietKiem(100000)
tk1.rut_tien(60000) 
tk2 = TaiKhoanThanhToan(100000)
tk2.rut_tien(50000)