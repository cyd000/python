# Created on iPad.
a=float(input('请输入快递重量：'))
print('地区编号：')
print('1:华东地区')
print('2:华南地区')
print('3:华北地区')
b=int(input('请输入地区编号：'))
if b==1:
    if a<=2:
        c=13
    else:
        c=3*a+7
elif b==2:
    if a<=2:
        c=12
    else:
        c=2*a+8
else:
    if a<=2:
        c=14
    else:
        c=4*a+6
print(f'快递费为{c}元')