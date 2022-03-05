#*Def trong Python:
# Cấu trúc:
# def tên hàm (tham số 1, tham số 2, ...) :
#     Câu lệnh 1 trong hàm
#     Câu lệnh 2 trong hàm
#     ...
#
#     return giá trị trả về
#ví dụ:
def add(a, b):
    x = a + b
    print(x)
    return x
# "def" là từ khóa dùng để khai báo hàm trong Python
# "add" là tên hàm(một chuỗi ký tự dùng để đặt tên đại diện cho hàm)
# "a" và "b" là các tham số
# return là từ khóa dùng để trả giá trị trả về từ hàm trong Python

#*Gọi hàm trong Python:
# Cấu trúc:
# tên hàm ( đối số 1, đối số 2,...)
#ví dụ:

def add(a, b):
    x = a + b
    return(x)

add(1, 2)
add(5, 6)
# Viết tên hàm, sau đó đặt các đối số (các giá trị truyền vào khi gọi hàm) ở giữa cặp dấu ngoặc đơn () và cách nhau bởi dấu phẩy ,. Các giá trị của đối số sẽ được dùng để truyền tham số trong python.