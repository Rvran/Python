# Python学习笔记-数据类型
# 单行注释
"""
多
行
注
释
"""

# 浮点运算时为避免小概率出错，引用decimal
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

# 数据类型-Boolean
num = True
num2 = False
print(num, type(num))
print(num2, type(num2))

# 数据类型转换
name = '然'
age = 23
# name（str）和age（int）不是同一种数据类型，需要将age转换为str数据类型str（age）才能正常拼接
# 否则会报错 TypeError: can only concatenate str (not "int") to str
print('我叫' + name + '，今年' + str(age) + '岁了')

# 将其他类型转换为int类型
print('-------将其他数据类型转换为int类型-----------------')
s1 = 128
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(int(s1), type(int(s1)))  # 将str转成int类型，字符串为数字串
print(int(f1), type(int(f1)))  # 将float转成int类型，舍弃小数部分，取整数
print(int(ff), type(int(ff)))  # 将Boolean转换为int，Ture→1，False→0

# 将其他类型转换为float类型
print('-------将其他数据类型转换为float类型-----------------')

# int类型转换为float类型，默认保留小数点一位
print(float(s1), type(float(s1)))
