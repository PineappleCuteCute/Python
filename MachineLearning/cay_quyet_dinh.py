#Đào Thành Mạnh đẹp trai


from sklearn import tree

#Bước 1: thu thập dữ liệu
#Bước 2: xử lý dữ liệu
#Bước 3: Training model
#Bước 4: Dự đoán kết quả
#Bước 5: đánh giá xem model có hiệu quả hay ko
my_tree = tree.DecisionTreeClassifier()
dactrung = [[1, 3, 3, 7],
            [5, 2, 4, 6],
            [1, 2, 4, 6],
            [5, 4, 4, 3],
            [1, 4, 4, 7],
            [3, 2, 3, 7],
            [3, 3, 3, 6],
            [5, 2, 2, 7]
            ]

nhan = [0, 1, 1, 0, 0, 0, 0, 1]

result = my_tree.fit(dactrung, nhan)

ket_qua = result.predict([[1, 4, 3, 6],
                     [1, 4, 3, 7]])

print(ket_qua)

