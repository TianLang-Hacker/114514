# 检查输入的内容是否是手机号

phonenum=input()
flag=True
asd=""

for ch in phonenum:
    if ch not in "1234567890":
        flag=False
    else:
        if ch !="":
            asd=asd+ch

result=""
if flag==True:
    result="Yes"
else:
    result="No"

print(result)