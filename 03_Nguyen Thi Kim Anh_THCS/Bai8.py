def tim_so_le_lon_nhat(a, b, c):
    le_nums = []
    if a % 2 != 0:
        le_nums.append(a)
    if b % 2 != 0:
        le_nums.append(b)
    if c % 2 != 0:
        le_nums.append(c)
    if not le_nums:
        return -1
    return max(le_nums)
print(tim_so_le_lon_nhat(13,6,45))

