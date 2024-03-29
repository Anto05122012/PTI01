class Khachhang:
    def __init__(self,makhachhang, tenkhachhang, tuoikhachhang, diachinha, stk):
        self.tenkhachhang = tenkhachhang
        self.ma_khach_hang = makhachhang
        self.tuoi_tho_khach_hang = tuoikhachhang
        self.dia_chi_thuong_tru_khach_hang = diachinha
        self.so_tai_khoan = stk
    
    def update(self, new_data:dict):
        for attribute, value in new_data. items():
            if value:
                setattr(self, attribute, value)

    def print_info():
        for khachhang in tongkhachhang:
            print(khachhang.tenkhachhang)
    def xoa_ten_khach_hang():
        remove_user = input('Nhập tên khách hàng bạn muốn xóa: ')
        for khachhang in tongkhachhang:
            if khachhang.tenkhachhang == remove_user:
                tongkhachhang.remove(khachhang)
    def cap_nhat_khach_hang():
        new_data = {'tenkhachhang': 'Nguyễn Ngọc Đức Cống'}
        ten_khachhang_1.update(new_data)
        print(ten_khachhang_1.tenkhachhang)

    
            
ten_khachhang_1 = Khachhang(72985,"Nguyễn Việt Long",18,'174 Đường Tên Lửa',3098756387)
ten_khachhang_2 = Khachhang(72095,"Nguyễn Việt Bồ Long",50,'176 Đường Tên Lửa',3098724187)
ten_khachhang_3 = Khachhang(72575,"Nguyễn Việt Mama Long",70,'174 Đường Tên Lửa',3098093387)
ten_khachhang_4 = Khachhang(70965,"Nguyễn Việt Daddy Long",75,'174 Đường Tên Lửa',3098566387)
tongkhachhang = [ten_khachhang_1,ten_khachhang_2,ten_khachhang_3,ten_khachhang_4]

ten_khachhang_5 = Khachhang(72763,"Nguyễn Việt Pé Long",5,'174 Đường Tên Lửa',3006756387)
tongkhachhang.append(ten_khachhang_5)
Khachhang.print_info()

# Khachhang.xoa_ten_khach_hang()

Khachhang.print_info()

Khachhang.cap_nhat_khach_hang()
