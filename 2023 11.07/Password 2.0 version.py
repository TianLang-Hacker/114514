#输入的密码是数字和字母的组合

passwd=input("输入密码：")

result=""
other_flag=True    #是否有数字和字母以外字符的标志
num_flag=False     #是否有数字的标志
char_flag=False    #是否有字母的标志
for ch in passwd:  
    #不能有数字字母以外的字符
    if ch not in "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        other_flag=False
    #必须有数字    
    if ch in "12345687890":
        num_flag=True
    #必须与字母
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        char_flag=True
if other_flag and num_flag and char_flag:
    result="是"
else:
    result="不是"

print(result)
