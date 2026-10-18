s = input('请输入您的身份证号码：')
year = s[6:10]
month = int(s[10:12])
day = int(s[12:14])
sex = '男' if int(s[16]) % 2 else '女'
print(f'您是{year}年{month}月{day}日出生的')
print('您的性别是：', sex)
print('您的身份证校验码是：', s[-1].upper())
