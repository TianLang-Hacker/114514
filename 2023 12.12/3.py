# # list--列表：[]
# myList=list
# print(myList)
# myList=[]
# print(myList)
# myList=[1,3,5,7,9]
# print(myList)
#
# # tuple--元组
# myTuple=tuple()
# print(myTuple)
# myTuple=()
# print(myTuple)
# myTuple=(123,324,46,657)
# print(myTuple)
#
# # set--集合：[]
# mySet=set()
# print(mySet)
# mySet={}
# print(mySet)
# mySet={321,654,987,18,87,14}
# print(mySet)
#
# # 利用集合去除列表中的重复值
# setl=set(myList)
# print(setl)
# myList=list(setl)
# print(myList)
# # 列表值可以修改
# myList[1]=100
# print(myList)
#
# # 元组不能修改值
# myTuple[1]=100
# print(myTuple)
#
# # 列表中的值有顺序



# 比赛计分系统：评委给分，去掉一个最高分，去掉一个最低分，然后输出平均分

# 输入评委分数录入
myList=[]
while True:
    num=int(input("输入评分："))
    myList.append(num)
    flag=input("结束录入请按N，按其他键继续")
    if flag.upper()=="N":
        break
print(myList)

# 处理：去掉一个最高分，去掉一个最低分，然后平均
maxNum=max(myList)
minNum=min(myList)
myList.remove(maxNum)
myList.remove(minNum)
avgNum=sum(myList)/len(myList)

# 输出 最终得分（平均分）
print("最终得分是：",avgNum)