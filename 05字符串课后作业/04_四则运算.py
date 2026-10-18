import random

count = 0
correct = 0
while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*', '/'])
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    else:
        answer = a / b
    user = input(f'{a}{op}{b}=\n')
    if user.lower() == 'q':
        break
    try:
        value = float(user)
    except ValueError:
        print('wrong')
        count += 1
        continue
    count += 1
    if abs(value - answer) < (0.005 if op == '/' else 1e-9):
        correct += 1
        print('right')
    else:
        print('wrong')
rate = correct / count * 100 if count else 0
print(f'共有 {count} 个题目，做对 {correct} 道，正确率为:{rate:.2f}%')
