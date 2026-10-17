# Created on iPad.
a=float(input('请输入您的身高(cm):'))
b=float(input('请输入您的体重（kg):'))
BMI=b/((a/100)*(a/100))
if BMI<18.5:
    print(f'您的BMI={BMI}，过瘦，正常范围：18.5-25')
elif BMI<=24.9:
    print(f'您的BMI={BMI}，正常')
else:
    print(f'您的BMI={BMI}，体重超重，正常范围：18.5-25，请增加锻炼。')