# # 检查输入的内容是否符合银行卡卡号的规则
# num=input()
# flag=num.isdigit()

# result=""
# if flag==True:
#     num=int(num)
#     if 1000000000000000<num<9999999999999999:
#         result="是"
#     else:
#         result="不是"
# else:
#     result="滚"

# print(result)


bankcard=input()
flag=True
newBankCardNo=""

for ch in bankcard:
    if ch not in "1234567890":
        flag=False
    else:
        if ch !="":
            newBankCardNo=newBankCardNo+ch

result=""
if flag==True:
    result="Yes"
else:
    result="No"

print(result)