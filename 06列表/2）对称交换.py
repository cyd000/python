import random
n=int(input("输入正整数n:"))
初始的=[]
for i in range(n):
    初始的+=[random.randint(0,99)]
交换后=list(reversed(初始的))
print(f"初始的：{初始的}")
print(f"交换后：{交换后}")
