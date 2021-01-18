a = 0
b = 10
num = [1, 22, 34, 5, 6, 7, 8, 9]

def aa(shu):
    for i in num:
        print(i)
        if i == shu:
            print("完成")
            break
        else:
            aa()

aa(1)