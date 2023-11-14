a=input("输入解密的内容：")

asd=ord("c")
result=""
for ch in a:
    code=ord(ch)                #取出字符的编码
    code=code-1145+asd               #将编码-1
    result=result+chr(code)     #将新的编码对应的字符保存起来

print("解密后是：",result)