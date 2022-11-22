import numpy as np
from matplotlib import pyplot as plt
# prepare data
A = [2,4,6,8,13,35,57,79]
b = [1,3,5,7,9,24,46,68]

#visualize data
plt.plot(A,b,"ro")

#re-arrange data
A = np.array([A]).T 
b = np.array([b]).T 
ones = np.ones((A.shape[0],1),dtype=np.int8) # tạo ma trận ones với giá trị toàn là 1, kích cỡ bằng số hàng của A
A = np.concatenate((A,ones), axis =1) # gộp ma trận A với ma trận Ones thành 2 hàng dọc

# hàm linear
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)

# chọn 2 điểm 
x0 = np.array([2,79]).T  # 2 và 79 là 2 giá trị đầu cuối của trục x 
y0 = x0*x[0,0] + x[1,0]

plt.plot(x0,y0)
print(x)
plt.show()

#test pull
#test GP

