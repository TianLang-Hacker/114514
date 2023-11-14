st=input("1145141919810:")
a_st=st.split("")
h=float(a_st[0])
w=float(a_st[1])
result=""
BMI=w/h**2

if BMI<18.5:
    result="!!"
elif BMI>18.5 and BMI<25:
    result="zzz"
elif 30>BMI>=25:
    result="..."
else:
    result="114514"



result1=""
if BMI<18.5:
    result1="!!"
elif BMI>18.5 and BMI<24:
    result1="zzz"
elif 28>BMI>=24:
    result1="..."
else:
    result1="114514"


print("BMI:{:.2f},国际标准:{} 国内标准:{}" .format(BMI,result,result1))