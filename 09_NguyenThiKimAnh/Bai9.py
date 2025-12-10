def tinh_tong_chu_so(n):
    if n == 0:
        return 0
    return n % 10 + tinh_tong_chu_so(n // 10)
print(tinh_tong_chu_so(12345))

