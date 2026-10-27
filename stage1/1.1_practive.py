# ===== 第一部分：变量 =====

# 赋值：把数据放进变量
name = "Alice"        # 字符串
age = 20              # 整数
height = 1.65         # 浮点数（小数）
is_student = True     # 布尔值（True/False）

# 使用：打印变量的值
print(name)           # 输出: Alice
print(age)            # 输出: 20
print(height)         # 输出: 1.65
print(is_student)     # 输出: True

# 变量可以重新赋值
age = 21
print(age)            # 输出: 21（覆盖了原来的20）

# 变量可以参与计算
next_year = age + 1
print(next_year)      # 输出: 22


# ===== 第二部分：数据类型 =====

# 用 type() 查看数据类型
print(type(42))          # 应该输出: <class 'int'>
print(type(3.14))        # 应该输出: <class 'float'>
print(type("hello"))     # 应该输出: <class 'str'>
print(type(True))         # 应该输出: <class 'bool'>
print(type(None))         # 应该输出: <class 'NoneType'>

# 类型转换
x = "123"
y = int(x)       # 字符串转整数
print(y + 1)     # 应该输出: 124

a = 3.7
b = int(a)       # 浮点转整数（直接砍掉小数）
print(b)         # 应该输出: 3

c = 100
d = str(c)       # 整数转字符串
print(d + "元")  # 应该输出: 100元



# ===== 第三部分：运算符 =====

# 算术运算符
a = 10
b = 3
print(a + b)    # 加法 → 13
print(a - b)    # 减法 → 7
print(a * b)    # 乘法 → 30
print(a / b)    # 除法 → 3.333...
print(a // b)  # 整除 → 3（只要整数部分）
print(a % b)    # 取余 → 1
print(a ** b)  # 10的3次方 → 1000

# 比较运算符
x = 5
y = 10
print(x == y)   # 等于 → False
print(x != y)   # 不等于 → True
print(x < y)    # 小于 → True

# 逻辑运算符
age = 25
has_id = True
print(age >= 18 and has_id)    # 两个都真 → True
print(age < 18 or has_id)      # 有一个真 → True
print(not has_id)              # 取反 → False

# 字符串运算
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)   # 拼接 → Hello World
print(s1 * 3)          # 重复3次 → HelloHelloHello
print(len(s1))         # 长度 → 5



# ===== 第四部分：输入输出 =====

# f-string 格式化输出（推荐用法）
score = 95
name = "李明"
print(f"{name} 的成绩是 {score} 分")
print(f"明年年龄：{age + 1} 岁")

# input 输入（运行时会等你打字）
your_name = input("请输入你的名字：")
your_age = input("请输入你的年龄：")
your_age = int(your_age)   # 转成整数才能计算

print(f"你好 {your_name}，今年 {your_age} 岁，明年 {your_age + 1} 岁")


#练习题
#一变量

city = "上海"
print(city)

city = "北京"
print(city)



a = 3 
b = 5
print(a)
print(b)

print("a b值交换后")
c = a
a = b
b = c
print(a)
print(b)


#二数据类型

print(type("abc"))
print(type(100))
print(type(3.14))
print(type(True))
print(type(None))

print(int("256") * 2)

print(int(9.8))

print(int(float("3.14")))



#第三组 运算符

print(17 // 3)
print("17除以三，取整数部分。")
print(f"{17 % 3},表示17除以三 取余")


print(2 ** 10)

score = 85
print(60 <= score <= 100)

print(not (3 > 1 and 5 < 3))

print("ha" * 3 + "!")




#第四组
name = input("请输入你的名字")
age = int(input("请输入你的年龄"))

print(f"{name}今年{age}岁，明年{age + 1}岁")


a = 99.9 #一件商品99.9元
b = (a * 3) * 0.8 #买三件，打八折。
print(f"三件打八折后一共：{b}元")
































































































