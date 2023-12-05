id=input()

result=""
length=len(id)        #得到身份证的长度
if length==18:
    result=="是18位"
    #1~17位只能是数字
    flag=0            #默认是17位数字
    for ch in id[0:17]:
        if ch not  in "1234567890":
            result="不是身份证号"
    flag=1
    #最后一位只能是数字或X或x
    if flag==0:          #如果前17位是数字，检查最后一位
        if id[-1] not in "1234567890Xx":
            result="不是身份证号"

else:
    result="不是身份证号"

print(result)