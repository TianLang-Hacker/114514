#输入的内容里是否有*

st=input("请输入：")

result="无*"

for ch in st:
    if ch=="*":
        result="是"
    else:
        result="不是"

print(result)