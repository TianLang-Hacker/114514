#C to F or F to C
#C to F：(F-32)÷1.8
#F to C：C×1.8+32

tempIn=input("你TM快点给老子输入符号（C/F）结尾的温度！：")

result="处理好了，给老子去看！"
if tempIn[-1]=="F":
    C=(float(tempIn[0:-1])-32)/1.8
    result=str(C)+"C"

elif tempIn[-1]=="C":
    F=float(tempIn[0:-1])*1.8+32
    result=str(F)+"F"

else:
     result="你TM打的什么鬼东西"

print(result)
input("任意键退出: ")