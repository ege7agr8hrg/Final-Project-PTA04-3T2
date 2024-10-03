class Hocsinh:
    def __init__(self, _hoten, _lop, _truong, _diemtoan, _diemvan, _diemanh):
        self.hoten = _hoten
        self.lop = _lop
        self.truong = _truong
        self.diemtoan = _diemtoan
        self.diemvan = _diemvan
        self.diemanh = _diemanh

    def GPA(self):
            return (self.diemtoan + self.diemvan + self.diemanh) / 3
    
class quanlyhs:
    def __init__(self):
          hs1 = hocsinh("Nguyen A", "PTA04", "Mindx", 10, 10 ,10)
          hs2 = hocsinh("Douglas Hogman", "PBQ04", "Rizzler school", 9, 9, 9)
          hs3 = hocsinh("Nguyen Co La", "DK90", "Bizz" 8, 7, 10)
          self.dshocsinh = [hs1, hs2, hs3]
    def xuatrahscogpacaonhat(self):
         GPAMAX = -1
         dshocsinhcaonhat = []
         for hs in self.dshocsinh:
              if hs.GPA() > GPAMAX:
                   dshocsinhcaonhat.clear()
                   dshocsinhcaonhat.append(hs)
                   GPAMAX = hs.GPA()
                if hs.GPA == GPAMAX:
                   dshocsinhcaonhat.append(hs)
            for hs in dshocsinhcaonhat:
              hs.getName()

test = quanlyhs()
test.xuatrahscogpacaonhat()