class TaiLieu:
    def __init__(self, ma_tai_lieu, nha_xuat_ban):
        self.ma = ma_tai_lieu
        self.nxb = nha_xuat_ban

    def thong_tin_chung(self):
        return f"Mã: {self.ma}, NXB: {self.nxb}"

class Sach(TaiLieu):
    def __init__(self, ma, nxb, tac_gia, so_trang):
        super().__init__(ma, nxb)
        self.tac_gia = tac_gia
        self.so_trang = so_trang

    def in_chi_tiet(self):
        print(f"[Sách] {self.thong_tin_chung()} - Tác giả: {self.tac_gia}")

class TapChi(TaiLieu):
    def __init__(self, ma, nxb, so_phat_hanh):
        super().__init__(ma, nxb)
        self.so_phat_hanh = so_phat_hanh

    def in_chi_tiet(self):
        print(f"[Tạp chí] {self.thong_tin_chung()} - Số PH: {self.so_phat_hanh}")

s = Sach("S001", "NXB Kim Đồng", "Tô Hoài", 150)
tc = TapChi("TC01", "NXB Giáo Dục", 52)

s.in_chi_tiet()
tc.in_chi_tiet()