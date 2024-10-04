print("Hello World")

print("床前明月光", end="")
print("疑是地上霜")

print('张三')

print("12" + "12")

print(30 % 2)

print(bool(""))		# False

print(bool("s"))	# Ture

print(str(111) == 111)

print(True == True)		# True
print(True == False) 	# False

print(bool("") == bool(0))	# True


# text = input("请输入你的年龄")
# print(text)

text = "我的名字叫{0}今年{1}岁".format("张三",18)
print(text)

name = "张三"
age = 18

text = f"我的名字{name}今年{age}岁"
print(text)

v2 = 2 and 4
print(v2)

name = "张三"
date = name.encode('utf-8')
print(date)