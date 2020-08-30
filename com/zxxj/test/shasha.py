len = 10
list = []
for i in range(len):# 输入
    list.append(int(input()))

dif = abs(list[0]-list[1])
index1 = 0
index2 = 1
for i in range(len):
    for j in range(i+1,len):
        a = abs(list[i]-list[j])
        if a < dif: # 比较、记录
            dif = a
            index1 = i
            index2 = j
print(list[index1],list[index2],dif) #输出


