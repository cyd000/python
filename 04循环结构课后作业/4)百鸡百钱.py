# Created on iPad.
num=0
for i in range(20):
    for j in range(34):
        k=100-i-j
        if i*5+j*3+k/3==100:
            num+=1
            print(f'买法{num}:公鸡{i}只，母鸡{j}只，小鸡{k}只')
print(f'共有{num}种买法')
                