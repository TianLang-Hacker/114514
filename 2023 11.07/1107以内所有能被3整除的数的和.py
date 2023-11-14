#计算1107以内所有能被3整除的数的和

total = 0
for i in range(1107):
    if i % 3 == 0:
        total=total+i

    print(total)