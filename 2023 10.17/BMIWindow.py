# usetk_calBMI.py


import tkinter




def onClick():
    st=E.get()
#    st=input("输入体重和身高(kg m)：")
    a_st=st.split(" ")
    W=float(a_st[0])
    H=float(a_st[1])
    result=""
    C=""
    BMI=W/(H*H)
    if BMI<18.5:
        result="偏瘦"
    elif BMI>18.5 and BMI<25:
        result="正常"
    elif BMI>25 and BMI<30:
        result="偏胖"
    else:
        result="肥胖"

    if BMI<18.5:
        C="偏瘦"
    elif BMI>18.5 and BMI<24:
        C="正常"
    elif BMI>24 and BMI<28:
        C="偏胖"
    else:
        C="肥胖"
    stText.set("BMI:{:.2f},按照国际标准是:{},按照国内标准是:{}".format(BMI,result,C))

#实例化一个窗体
myWindow=tkinter.Tk()
#设置窗体属性
myWindow.title("BMI")
myWindow.geometry("800x450+50+50")
#标签
stText=tkinter.StringVar("")
L=tkinter.Label(myWindow,text="",bg="#AACCBB",font=(30),textvariable=stText)
#显示标签
L.pack()
#输入框
E=tkinter.Entry(myWindow,font=("Microsoft YaHei",20))
#显示输入框
E.pack()
#按钮
B=tkinter.Button(myWindow,text="GO",font=("Microsoft YaHei",16),command=onClick)
#显示按钮
B.pack()


myWindow.mainloop()
