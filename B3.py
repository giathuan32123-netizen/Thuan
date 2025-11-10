can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tí", "Sửu", "Dần", "Mẹo", "Thìn", "Tỵ", "Ngọ", "Mùi"]

nam = int(input("Nhập năm dương lịch: "))

cann = nam % 10
chii = nam % 12
match cann:
    case 0:
        ten_can = "Canh"
    case 1:
        ten_can = "Tân"
    case 2:
        ten_can = "Nhâm"
    case 3:
        ten_can = "Quý"
    case 4:
        ten_can = "Giáp"
    case 5:
        ten_can = "Ất"
    case 6:
        ten_can = "Bính"
    case 7:
        ten_can = "Đinh"
    case 8:
        ten_can = "Mậu"
    case 9:
        ten_can = "Kỷ"
match chii:
    case 0:
        ten_chi = "Thân"
    case 1:
        ten_chi = "Dậu"
    case 2:
        ten_chi = "Tuất"
    case 3:
        ten_chi = "Hợi"
    case 4:
        ten_chi = "Tí"
    case 5:
        ten_chi = "Sửu"
    case 6:
        ten_chi = "Dần"
    case 7:
        ten_chi = "Mẹo"
    case 8:
        ten_chi = "Thìn"
    case 9:
        ten_chi = "Tỵ"
    case 10:
        ten_chi = "Ngọ"
    case 11:
        ten_chi = "Mùi"

nam_al = can[cann] + " " + chi[chii]
print(f"Năm {nam} là năm {nam_al}")



