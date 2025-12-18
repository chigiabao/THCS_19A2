class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_chu_vi(self):
        return (self.dai + self.rong) * 2

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def ve_hinh(self):
        print(f"Vẽ hình {self.dai}x{self.rong}:")
        for i in range(self.rong):
            print(" * " * self.dai)
hcn = HinhChuNhat(5, 3)
print(f"Chu vi: {hcn.tinh_chu_vi()}, Diện tích: {hcn.tinh_dien_tich()}")
hcn.ve_hinh()