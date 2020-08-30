import cv2 #导入opencv库
import numpy as np
import pandas as pd
import csv

# 读取一张图片，地址不能带中文
# imgviewx=cv2.imread("remu512.png",cv2.IMREAD_GRAYSCALE)
imgviewx=cv2.imread("r256.png")

# cv2.namedWindow("东小东标题")

# cv2.imshow("东小东标题",imgviewx)

cv2.waitKey(0)
cv2.destroyAllWindows()

#获取图片信息
#一个像素有三个通道，BGR
print(imgviewx.shape)#输出：(1080, 1920, 3) 高像素，宽像素，通道数
print(imgviewx.size) #总通道数=高* 宽* 通道数
print(imgviewx.dtype)# uint8  3个通道每个通道占的位数（8位，一个字节）
print(imgviewx) #输出效果视乎与下条相同
print(np.array(imgviewx)) #输出每个像素点的参数（ B , G , R )

p = []
#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 导入CSV安装包
import csv

# 1. 创建文件对象
f = open('r256rbg.csv','w',encoding='utf-8',newline="")
# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)
# 3. 构建列表头
csv_writer.writerow(["x","y","b","g","r"])
# 4. 写入csv文件内容
csv_writer = csv.writer(f)

# 遍历输出图片位置、颜色
gx,kx,tx=imgviewx.shape
for g in range(0,gx):
    for k in range(0, kx):
        # print(g,k,imgviewx[g,k])
        csv_writer.writerow([k,gx-g,imgviewx[g,k][0],imgviewx[g,k][1],imgviewx[g,k][2]]) #y倒置,输出bgr

# 5. 关闭文件
f.close()
# print(p)
# writerCSV=pd.DataFrame(data=p)
# writerCSV.to_csv('./no_fre.csv',encoding='utf-8')