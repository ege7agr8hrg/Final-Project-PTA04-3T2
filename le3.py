class PhanSo:
    # ham khoi tao
    def __init__(self, _tuso = 0, _mauso = 1):
        self.tuso = _tuso
        self._mauso = _mauso
    # ham nhap
    def _input(self):
        l = input().split()
        self.tuso = int(l[0])
        self.mauso = int(l[1])
    # ham xuat
    def _ouput(self):
        print(str(self.tuso) + "/" + str(self.mauso))
    def xuatTuSo(self):
        print(self.tuso)
    def xuatMauSo(self):
        print(self.mauso)
    def XuatPsNghichDao(self):
        print(str(self.mauso) + "/" + str(self.tuso))
    def XuatPsRutGon(self):
        tumoi, maumoi = self.tuso, self.mauso
        mauchung = 2 
        while tumoi >= mauchung and maumoi >= mauchung:
            while tumoi % mauchung == 0 and maumoi % mauchung == 0:
                tumoi /= mauchung
                maumoi /= mauchung
            mauchung += 1
        return PhanSo(int(tumoi), int(maumoi))
    def PsPro(self):
        a = self.tuso
        b = self.mauso
        tusomoi = a*a + b*b
        mausomoi = a*b
        PhanSo(tusomoi, mausomoi).XuatPsRutGon()._ouput()
        
ps = PhanSo()
ps._input()
ps._ouput
ps.xuatTuSo()
ps.xuatMauSo()
ps.XuatPsNghichDao()
ps.XuatPsRutGon()
ps.PsPro()


class car:
    def __init__(self,_brand = "None", _model = "None", _price = "None"):
        self.brand = _brand
        self.model = _model
        self.price = _price
    def show(self):
        print("Brand", self.brand)
        print("Model", self.model)
        print("Price", self.price)

car1= car()
car1.show()

car2 = car("Astron Martin", "Valkyrie", 3500000)
car2.show ()