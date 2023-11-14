#加密 不能被别人破解

#得到明文
st=input("请输入加密的内容：")

#加密处理
asd=ord("c")

result=""
for ch in st:
    code=ord(ch)                #取出字符的编码
    code=code+1145-asd            #将编码+114514
    result=result+chr(code)     #将新的编码对应的字符保存起来

#输出密文
print("密文是：",result)
