class DongVat:
    def __init__(self, ten, can_nang):
        self.ten = ten
        self.can_nang = can_nang

    def keu(self):
        print("...")

class Cho(DongVat):
    def __init__(self, ten, can_nang, loai_long):
        super().__init__(ten, can_nang)
        self.loai_long = loai_long 

    def keu(self):
        print("Gâu gâu!")

class Meo(DongVat):
    def keu(self):
        print("Meo meo!")
    
    def leo_cay(self): 
        print(f"{self.ten} đang leo cây thoăn thoắt.")
dog = Cho("Lu", 10, "Xù")
cat = Meo("Mimi", 3)
dog.keu()
cat.keu()
cat.leo_cay()
