# Câu 1 :B
# Câu 2 :B
# Câu 3 :A
# Câu 4 :B
# Câu 5 :D
# Câu 6 :A
# Câu 7 :B
# câu 8 :D
# câu 9 :B
# Câu 10 :B

# Thực hành
class HocSinh:
    def __init__(self, _ten = "chuabiet", _diachi = "chuabiet", _chieucao = 0, _cannang = 0, _hocluc = "chuabiet"):
        self.ten = _ten
        self.diachi = _diachi
        self.chieucao = _chieucao
        self.cannang = _cannang
        self.hocluc =  _hocluc
        
    def show(self):
        print(" Ten hoc sinh", self.ten)
        print("Dia chi", self.diachi)
        print("Chieu cao", self.chieucao)
        print("Can nang", self.cannang)
        print("Hoc luc", self.hocluc)

    def chuyennha(self, diachimoi):
        self.diachi = diachimoi
    def khamsuckhoe(self,chieucaomoi,cannangmoi):
        self.chieucao = chieucaomoi
        self.cannang = cannangmoi
hs1 = HocSinh("Đíc","Sài Gòn","137", "40", "Trung Bình")
hs1.show()
hs1.chuyennha("Hà Nội")
hs1.khamsuckhoe(140, -183290)
hs1.show()