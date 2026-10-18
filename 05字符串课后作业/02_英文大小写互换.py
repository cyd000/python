s = input('请输入一段英文：')
result = ''
for ch in s:
    if 'a' <= ch <= 'z':
        result += ch.upper()
    elif 'A' <= ch <= 'Z':
        result += ch.lower()
    else:
        result += ch
print(result)
