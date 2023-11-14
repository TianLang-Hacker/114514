#输入密码，8~16位，有大小写字母，特殊符号和数字的任意三种组合

passwd=input("输入密码：")

result=""
char_flag=0
spec_flag=0
num_flag=0
Char_flag=0
length=len(passwd)   #获取密码的长度

if length>=8 or length<=16:
    result="不符合"
else:
    for ch in passwd:
        code=ord(ch)
        #可以有大写
        if code>=65 and code<=90:
    #if ch in "!@#$%^&*()_-=+\|]}[{;:'<,.>/?`~":
            char_flag=1
            
        #可以有小写
        if code>=97 and code<=122:
            char_flag=1

        #可以有特殊符号
        if ch not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
            spec_flag=1

        #必须有数字    
        if ch in "12345687890":
            num_flag=1

        #满足任意三种
        count=Char_flag + char_flag + num_flag + spec_flag
        if count==3:
            result="是"
        else:
            result="不是"

print(result)
