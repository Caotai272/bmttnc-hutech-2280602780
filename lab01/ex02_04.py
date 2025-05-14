# Tạo một danh sách rỗng để lưu kết quả
j = []
# Duyệt qua tất cả các số từ 2000 đến 3200, kiểm tra nếu số đó chia hết cho 7 nhưng không phải là bội số của 5
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
# In danh sách kết quả, các số được phân tách bởi dấu phẩy
print(','.join(j))
