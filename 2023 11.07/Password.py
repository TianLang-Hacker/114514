#password
#判断输入的密码是否是6位数字

passwd=input("输入密码，6位数字")

result="是"
if len(passwd)==6:
    for ch in passwd:
        if ch not in "1234567890":
            result="不是"
else:
    result="不是"

print(result)

