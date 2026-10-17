# Created on iPad.
i=int(input('请输入正方形的边长：'))
for j in range(1,i+1):
    print('*',end=' ')
print()
for k in range(1,i-1):
    print('*',end=' ')
    for r in range(1,i-1):
        print(' ',end=' ')
    print('*')
for s in range(1,i+1):
    print('*',end=' ')
