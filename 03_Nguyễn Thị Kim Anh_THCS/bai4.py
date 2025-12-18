class XeHoi:
    def __init__(self, hang, mau, gia):
        self.hang = hang
        self.mau = mau
        self.gia = gia
        self.trang_thai = "Đang tắt máy"

    def khoi_dong(self):
        self.trang_thai = "Đang nổ máy"
        print(f"Xe {self.hang}: Grừ grừ... Đã khởi động.")

    def chay(self):
        if self.trang_thai != "Đang tắt máy":
            self.trang_thai = "Đang chạy"
            print(f"Xe {self.hang} màu {self.mau} đang lăn bánh trên đường.")
        else:
            print("Xe chưa nổ máy, không chạy được!")

    def dung(self):
        self.trang_thai = "Đã dừng"
        print("Kít... Xe đã dừng lại.")
xe = XeHoi("Toyota", "Đen", 1000)
xe.khoi_dong()
xe.chay()
xe.dung()