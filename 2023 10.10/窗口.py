import tkinter

def onClick():
    #print("1145141919810")
    st=myEntry.get()
    #print(wdnmd1)
    
    
    #处理
    result=""
    num=int(st)
    if num%7==0:
        result="Yes"
    else:
        result="No"

#输出
    stText.set(st)
#窗口实体化

#输出
stText=tkinter.StringVar("")

#窗口
myWindow=tkinter.Tk()
myWindow.title("WDNMD!")
myWindow.geometry("1280x720+0+0")

#显示
myBtn=tkinter.Button(myWindow,text="WDNMD!",font=("Arail",20),command=onClick)  #按钮
myEntry=tkinter.Entry(myWindow,font=("Arail",20))   #输入框
myLabel=tkinter.Label(myWindow,background="#114514",font=("Arail",20))   #标签


myEntry.pack()  #输入框显示出来
myBtn.pack()   #按钮显示出来
myLabel.pack()  #标签显示出来
