# Python学习笔记-input函数

# 输入函数input
age = input('你今年几岁了？\n')
print(age, type(age))

# 输入两个数，算和
num1 = input('输入第一个数：')
num2 = input('输入第二个数：')
result = float(num1) + float(num2)  # 注意input的数据类型，默认为str不能直接相加
print('和为：', result)
