def kiem_tra_so_armstrong(n):
    if not isinstance(n, int):
        if n <= 0:
            return False
        original = n
        tong = 0
        while n > 0:
            chu_so = n % 10
            tong += chu_so ** 3
            n //= 10
            return tong == original 
        
