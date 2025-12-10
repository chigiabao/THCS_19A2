def giai_phuong_trinh_bac_nhat(a, b):
    if a != 0:
        x = -b / a
        print(f"Nghiệm của phương trình là x = {x}")
    elif b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
