航班数=5
航班预定表=[[1,2,10],[2,3,20],[2,5,25]]
answer1=[]
for i in range(5):
    if 航班预定表[0][0]<=i+1<=航班预定表[0][1]:
        answer1.append(航班预定表[0][2])
    else:
        answer1.append(0)
answer2=answer1.copy()
for i in range(5):
    if 航班预定表[1][0]<=i+1<=航班预定表[1][1]:
        answer2[i]+=航班预定表[1][2]
answer3=answer2.copy()
for i in range(5):
    if 航班预定表[2][0]<=i+1<=航班预定表[2][1]:
        answer3[i]+=航班预定表[2][2]
print(f"航班数={航班数}，航班预定表={航班预定表}\nanswer1={answer1}\nanswr2={answer2}\nanswer3={answer3}\n\n座位总数={answer3}")
