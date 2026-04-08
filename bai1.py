class HocVien:
    # a) Constructor + thuộc tính
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) show info
    def show_info(self):
        print("Họ tên:", self.ho_ten)
        print("Ngày sinh:", self.ngay_sinh)
        print("Email:", self.email)
        print("Điện thoại:", self.dien_thoai)
        print("Địa chỉ:", self.dia_chi)
        print("Lớp:", self.lop)
        print("----------------------")

    # c) change info (có mặc định)
    def change_info(self, dia_chi="Hà Nội", lop="IT12.x"):
        self.dia_chi = dia_chi
        self.lop = lop


# d) Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng
    hv = HocVien(
        "Nguyễn Văn A",
        "10/05/2003",
        "a@gmail.com",
        "0123456789",
        "Hải Phòng",
        "IT11A"
    )

    print("Thông tin ban đầu:")
    hv.show_info()

    # Change với mặc định
    hv.change_info()
    print("Sau khi change (mặc định):")
    hv.show_info()

    # Change với giá trị khác
    hv.change_info("TP.HCM", "IT12B")
    print("Sau khi change (tùy chỉnh):")
    hv.show_info()