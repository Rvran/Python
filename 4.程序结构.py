# Python学习笔记-程序结构
# 三大结构：顺序结构 选择结构 循环结构

# 对象的布尔值，Python一切皆为对象，所有对象都有一个布尔值，获取布尔值：bool()
# 分支结构：单分支结构 双分支结构 多分支结构

# 选择结构：单分支结构：if用法
money = 2000
print("您当前的账户余额为", money)
case = float(input("请输入取款金额："))
balance = money - case
if case <= money:
    print("取款成功！")
    print("当前账户余额为：", balance)
elif case >= money:
    print("余额不足！！")
    print("您当前余额为：", money)

# 选择结构：双分支结构：if...else用法,if可以为多个，else只能一个
print("输入一个整数，判断是奇数还是偶数")
num = int(input("请输入一个整数："))
if num is not int:
    print("请输入整数！！")
if num is int:
    if num % 2 == 0:
        print(num, "为偶数")

    else:
        print(num, "该整数为奇数")
