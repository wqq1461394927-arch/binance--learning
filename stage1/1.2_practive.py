# 一   ===== 字符串 =====

s = "Hello World"

# 取单个字符（从0开始数）
print(s[0])     # H（第0个）
print(s[6])     # W（第6个）

# 切片（取一段）
print(s[0:5])   # Hello（从0到5，不包含5）
print(s[6:])    # World（从6到最后）
print(s[:5])    # Hello（从开头到5）

# 常用操作
print(len(s))       # 长度 → 11
print(s.upper())    # 全大写 → HELLO WORLD
print(s.lower())    # 全小写 → hello world
print(s.replace("World", "Python"))  # 替换 → Hello Python
print(s.split(" ")) # 按空格切开 → ['Hello', 'World']
print(s.strip())    # 去掉首尾空格


#s[:] 就是整个字符串，等于没切。冒号左边的包含，右边的不包含。但是 冒号左边不写 = 从第0位开始。冒号右边不写 = 取到最后一位。


# 二    ===== 列表 list =====

# 创建列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]

# 取元素（从0开始）
print(fruits[0])     # 苹果
print(fruits[1])     # 香蕉

# 取一段（切片，跟字符串一样）
print(fruits[1:3])   # ['香蕉', '橙子']

# 改元素
fruits[0] = "西瓜"
print(fruits)        # ['西瓜', '香蕉', '橙子', '葡萄']

# 加元素
fruits.append("芒果")
print(fruits)        # ['西瓜', '香蕉', '橙子', '葡萄', '芒果']

# 删除元素
del fruits[1]
print(fruits)        # ['西瓜', '橙子', '葡萄', '芒果']

# 列表长度
print(len(fruits))   # 4

# 数字列表
nums = [10, 20, 30, 40, 50]
print(max(nums))     # 最大值 → 50
print(min(nums))     # 最小值 → 10
print(sum(nums))     # 总和 → 150



#  三     ===== 字典 dict =====

# 创建字典（键值对）
student = {
    "name": "小明",
    "age": 20,
    "major": "区块链"
}

# 取值（用键）
print(student["name"])    # 小明
print(student["age"])     # 20

# 改值
student["age"] = 21
print(student)            # age 变成 21

# 加新键值对
student["school"] = "四川职业技术学院"
print(student)

# 删除
del student["major"]
print(student)

# 判断有没有某个键
print("name" in student)      # True
print("major" in student)     # False（已删除）

# 常用
print(len(student))            # 有几个键值对
print(student.keys())         # 所有键
print(student.values())        # 所有值



# 四  ===== 补充：字符串进阶 =====
s = "Hello World"
print(s[-1])       # 最后一个字符 → d
print(s[::-1])     # 反转 → dlroW olleH
print(s.startswith("Hello"))   # True
print(s.endswith("World"))     # True

# 五  ===== 补充：列表进阶 =====
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                # 升序 → [1, 1, 2, 3, 4, 5, 6, 9]
print(nums)
nums.sort(reverse=True)    # 降序
print(nums)
print(nums.index(5))       # 找5在第几位
print(nums.count(1))       # 1出现了几次

# 六   ===== 补充：元组 tuple =====
t = (1, 2, 3)
print(t[0])     # 跟列表一样取值
# t[0] = 99      # ❌ 报错！元组不能改
a, b, c = t     # 解包赋值
print(a, b, c)

# 七   ===== 补充：集合 set =====
data = [1, 2, 2, 3, 3, 3]
unique = set(data)       # 去重 → {1, 2, 3}
print(unique)
print(list(unique))      # 转回列表 → [1, 2, 3]

# 集合运算
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 | s2)    # 并集 → {1, 2, 3, 4}
print(s1 & s2)    # 交集 → {2, 3}
print(s1 - s2)    # 差集 → {1}


     













































