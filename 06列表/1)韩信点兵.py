print("今有一个数，")
a=int(input("若用3除的余数为："))
b=int(input("若用5除的余数为："))
c=int(input("若用7除的余数为："))
可能的数=[i for i in range(1000) if i%3==a and i%5==b and i%7==c]
print(f"在0-1000中有这样的数：\n{可能的数}")
