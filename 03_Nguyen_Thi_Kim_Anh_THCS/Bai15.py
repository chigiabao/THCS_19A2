def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
print("Các số nguyên tố trong koảng 100 đến 500: ")
for num in range(100, 501):
    if la_so_nguyen_to(num):
        print(num, end=" ")