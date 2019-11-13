#99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,'x',i,'=',j*i,end='\t')
    print()

#冒泡排序
a = [3, 5, 7, 1, 4, 34, 678, 2, 167, 899, 43, 11, 9, 345]
length = len(a)
for i in range(length - 1, 0, -1):
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = [j + 1], a[j]
print(a)
