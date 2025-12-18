class TaiKhoanNganHang:
    def __init__(self, so_tk, ten_chu_tk):
        self.so_tk = so_tk
        self.ten_chu_tk = ten_chu_tk
        self.__so_du = 0  

    def gui_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"Đã gửi {so_tien}. Số dư mới: {self.__so_du}")
        else:
            print("Số tiền gửi không hợp lệ.")

    def rut_tien(self, so_tien):
        if 0 < so_tien <= self.__so_du:
            self.__so_du -= so_tien
            print(f"Đã rút {so_tien}. Số dư còn lại: {self.__so_du}")
        else:
            print("Giao dịch thất bại (Số dư không đủ hoặc tiền rút sai).")

    def kiem_tra_so_du(self):
        return self.__so_du
tk = TaiKhoanNganHang("123456", "Nguyen Van A")
tk.gui_tien(1000)
tk.rut_tien(200)
tk.rut_tien(5000) 