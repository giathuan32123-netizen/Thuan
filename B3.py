1
can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọ", "Mùi"]
nam = int(input("Nhập năm dương lịch: "))
cann= nam % 10
chii = nam % 12
print(f"Năm {nam} là năm {can[cann]} {chi[chii]}")