s = input('请输入一段英文：')
positions = []
for i in range(len(s) - 3):
    if s[i:i + 4].lower() == 'rose':
        positions.append(i)
print(f'总共有{len(positions)}个玫瑰，出现的序号为：')
for i in positions:
    print(i)
