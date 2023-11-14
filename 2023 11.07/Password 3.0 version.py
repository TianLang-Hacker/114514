#输入的密码，8~16位大小写字母，数字和特殊符号的组合

passwd=input("输入密码：")

result=""
char_flag=False
spec_flag=False
num_flag=False
Char_flag=False
length=len(passwd)   #获取密码的长度

if length>=8 and length<=16:
    for ch in passwd:
        #必须有大写
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    #if ch in "!@#$%^&*()_-=+\|]}[{;:'<,.>/?`~":
            char_flag=True
            
        #必须有小写
        if ch in "abcdefghijklmnopqrstuvwxyz":
            char_flag=True

        #必须有特殊符号
        if ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
            spec_flag=True

        #必须有数字    
        if ch in "12345687890":
            num_flag=True

        if Char_flag and num_flag and char_flag and spec_flag:
            result="是"
        else:
            result="不是"
else:
    result="不是"


print(result)
