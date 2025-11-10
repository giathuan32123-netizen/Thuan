
can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọ", "Mùi"]
nam = int(input("Nhập năm dương lịch: "))
can_index = nam % 10
chi_index = nam % 12
print(f"Năm {nam} là năm {can[can_index]} {chi[chi_index]}")