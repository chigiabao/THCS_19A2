from abc import ABC, abstractmethod
class IPayment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(IPayment):
    def pay(self, amount):
        print(f"Đang thanh toán {amount} bằng Tiền mặt tại quầy.")

class EWalletPayment(IPayment):
    def pay(self, amount):
        print(f"Đang mở App ví điện tử... Thanh toán {amount} thành công.")
def xu_ly_don_hang(amount, payment_method: IPayment):
    payment_method.pay(amount)

xu_ly_don_hang(500000, CashPayment())
xu_ly_don_hang(200000, EWalletPayment())