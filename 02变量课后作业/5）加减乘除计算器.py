# Created on iPad.
a=int(input('请输入第一个数字：'))
b=input('运算符：+,-,*,/')
c=int(input('请输入第二个数字：'))
if b=='+':
    print(f'运算结果：{a+c}')
elif b=='-':
    print(f'运算结果：{a-c}')
elif b=='*':
    print(f'运算结果：{a*c}')
else:
    print(f'运算结果：{a/c}')