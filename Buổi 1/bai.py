class ChuNhat:
    def __init__(self, ChieuDai, ChieuRong):
        self.ChieuDai = ChieuDai
        self.ChieuRong = ChieuRong
    def ChuVi(self):

        return  (self.ChieuDai+self.ChieuRong)*2
    def DienTich(self):
        DienTich = self.ChieuDai*self.ChieuRong
        return DienTich

HinhChuNhat = ChuNhat(5,9)
print(HinhChuNhat.ChuVi())
print(HinhChuNhat.DienTich())