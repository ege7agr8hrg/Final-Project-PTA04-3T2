class AnimeItem:
    def __init__ (self, maphim, ten, ngay, diem, link):
        self.maphim = maphim
        self.ten = ten
        self.ngay = ngay
        self.diem = diem
        self.link = link
    
    def capnhat (self, new_dict : dict):
        for attribute, value in new_dict.items():
            if value:
                setattr(self, attribute, value)

