import tkinter

def onClick():
    st = E.get()
    try:
        a_st = st.split(" ")
        if len(a_st) != 2:
            raise ValueError("输入格式不正确，请输入体重和身高，用空格分隔。")
        W = float(a_st[0])
        H = float(a_st[1])
        if W <= 0 or H <= 0:
            raise ValueError("体重和身高必须为正数。")
        
        result = ""
        C = ""
        BMI = W / (H * H)
        
        if BMI < 18.5:
            result = "偏瘦"
        elif 18.5 <= BMI < 24:
            result = "正常"
        elif 24 <= BMI < 28:
            result = "偏胖"
        else:
            result = "肥胖"

        stText.set("BMI: {:.2f}, 按照国际标准是: {}, 按照国内标准是: {}".format(BMI, result, C))
    except ValueError as e:
        stText.set("错误: " + str(e))


myWindow = tkinter.Tk()
myWindow.title("BMI")
myWindow.geometry("800x450+50+50")

stText = tkinter.StringVar()
L = tkinter.Label(myWindow, textvariable=stText, bg="#AACCBB", font=("Microsoft YaHei", 20))
L.pack()

E = tkinter.Entry(myWindow, font=("Microsoft YaHei", 20))
E.pack()

B = tkinter.Button(myWindow, text="GO", font=("Microsoft YaHei", 16), command=onClick)
B.pack()

myWindow.mainloop()
