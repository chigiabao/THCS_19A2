def la_so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            tong += i
    return tong
print(tinh_tong_so_hoan_hao(1,10))